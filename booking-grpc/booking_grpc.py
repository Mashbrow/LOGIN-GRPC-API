from flask import Flask, render_template, request, jsonify, make_response
import requests
import json
import time
import grpc
import showtime_pb2
import showtime_pb2_grpc
import booking_pb2_grpc
import booking_pb2
from concurrent import futures
from werkzeug.exceptions import NotFound
from operator import itemgetter

### Modifying the REST service to become a GRPC Service 
class BookingServicer(booking_pb2_grpc.BookingServicer):

   def __init__(self):
      """
         Load Database
      """
      with open('{}/data/bookings.json'.format("."), "r") as jsf:
               self.db = json.load(jsf)["bookings"]

   
   def GetJson(self, request, context):
      """
         Get all bookings
      """
      for booking in self.db:
         yield booking_pb2.BookingData(userid = booking['userid'], dates=booking['dates'])
      
   def GetBookingForUser(self, request, context):
      """
         Get bookings of a user speficying an id
      """
      #Simulating computation time
      time.sleep(3)
      for booking in self.db:
         if booking["userid"]==request.id:
            print("Booking found!")
            return booking_pb2.BookingData(userid=booking["userid"], dates=booking['dates'])
      
      return booking_pb2.BookingData(userid="", dates=[])

   def AddBookingByUser(self, request, context):
      """
         Add booking of a movie for user spefifying its id
      """
      #Debugging use
      print("yes:",request)
      ### Check that the movie is scheduled
      ##GRPC Request to the Showtime API
      schedules = []
      with grpc.insecure_channel('dns:///showtime:3002') as channel:
         stub = showtime_pb2_grpc.ShowtimeStub(channel)
         allSchedule = stub.GetSchedule(showtime_pb2.Empty())
         for schedule in allSchedule:
            schedules.append({"date": schedule.date, "movies":schedule.movies})
         channel.close()
      
      sch_dates = [sch["date"] for sch in schedules]
      if request.date not in sch_dates:
         print("Date not found")
         return booking_pb2.BookingData(userid="", dates =[])
      sch_idx = sch_dates.index(request.date)
      if request.movieid not in schedules[sch_idx]["movies"]:
         print("Error: movie not scheduled at this date")
         return booking_pb2.BookingData(userid="", dates =[])
      
      ## Create and add the booking if so
      for b in self.db:
         if b["userid"] == request.userid:
            dates = [b_["date"] for b_ in b["dates"]]
            if request.date in dates:
               idx = dates.index(request.date)
               if request.movieid in b["dates"][idx]["movies"]:
                  print("Error: an exisiting item already exists")
                  return booking_pb2.BookingData(userid="", dates=[])
               b["dates"][idx]["movies"].append(request.movieid)
               return booking_pb2.BookingData(userid=b["userid"], dates=b['dates'])
            to_push = {"date" : request.date, "movies" : [request.movieid]}
            b["dates"].append(to_push)
            return booking_pb2.BookingData(userid=b["userid"], dates=b['dates'])


   

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    booking_pb2_grpc.add_BookingServicer_to_server(BookingServicer(), server)
    server.add_insecure_port('[::]:3005')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
