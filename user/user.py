from flask import Flask, render_template, request, jsonify, make_response
import grpc, movie_pb2, movie_pb2_grpc
import requests
import json
from werkzeug.exceptions import NotFound

app = Flask(__name__)

#Init Config
PORT = 3004
HOST = '0.0.0.0'

#Load database
with open('{}/data/users.json'.format("."), "r") as jsf:
   users = json.load(jsf)["users"]

#Index route
@app.route("/", methods=['GET'])
def home():
   return "<h1 style='color:blue'>Welcome to the User service!</h1>"

#Get all users
@app.route("/user", methods=['GET'])
def get_json():
   return make_response(jsonify(users), 200)

#Get user by specifying id in path
@app.route("/user/<userid>", methods=['GET'])
def get_average_user_rating(userid):
   #Find user
   r_sum = 0
   cond = False
   for element in users:
      if userid == element["id"]:
         cond = True
   if not cond:
      return make_response(jsonify({"error":"no user found"}), 400)

   #Request booking api (REST) to get bookings of the user
   host_ = 'http://' + request.host.split(':')[0]
   request_booking = requests.get(host_ + ':' + '3003'+'/booking/'+str(userid))
   if request_booking.ok : 
      bookings = request_booking.json()
   else:
      return make_response({"error":"no movies booked for that user"}, 409)
   
   #Request movie api (grpc)to get all movies
   movies_list = []
   with grpc.insecure_channel('localhost:3001') as channel:
      stub = movie_pb2_grpc.MovieStub(channel)
      allMovies = stub.GetListMovies(movie_pb2.Empty())
      for movie in allMovies:
         movies_list.append({"id": movie.id, "rating":movie.rating})
      channel.close()

   #Fetch movies that were booked by the user and get average rating     
   booked_movies = []
   for date in bookings["dates"]:
      booked_movies += date["movies"]

   for b_movie in booked_movies:
      for m in movies_list:
         if b_movie == m["id"]:
            r_sum += m["rating"]

   average = r_sum/len(booked_movies)      
   return make_response(jsonify({"average_rating":average}), 200)

if __name__ == "__main__":
   print("Server running in port %s"%(PORT))
   app.run(host=HOST, port=PORT)
