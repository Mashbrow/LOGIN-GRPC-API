import grpc

import booking_pb2
import booking_pb2_grpc


def get_booking_for_user(stub,userid):
    """
        Request booking (GRPC) service to get bookings of a user given an id
        Argument:
            - userid: booking_pb2.UserId, the id of a user
    """
    bookings = stub.GetBookingForUser(userid)
    print(bookings)

def get_json(stub):
    """
        Request booking (GRPC) service to get all the bookings in db
    """
    allbookings = stub.GetJson(booking_pb2.EmptyBooking())
    for b in allbookings:
        print("Booking of user %s" % (b.userid))

def add_booking_by_user(stub, new_booking):
    """
        Add booking for a specific user
        Argument:
            - new_booking: booking_pb2.NewBookingForUser, the booking to be added
    """
    bookings = stub.AddBookingByUser(new_booking)
    print(bookings)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('dns:///booking-grpc:3005') as channel:
        stub = booking_pb2_grpc.BookingStub(channel)

        print("-------------- GetBookingById --------------")
        bookingUser = booking_pb2.UserId(id="chris_rivers")
        print(bookingUser.id)
        get_booking_for_user(stub, bookingUser)
        
        print("-------------- GetListBooking --------------")
        get_json(stub)

        print("-------------- AddBookingForUser --------------")
        new_booking = booking_pb2.NewBookingForUser(userid="chris_rivers", movieid="720d006c-3a57-4b6a-b18f-9b713b073f3c", date="20151130")
        print(new_booking)
        add_booking_by_user(stub, new_booking)

    channel.close()

if __name__ == '__main__':
    run()
