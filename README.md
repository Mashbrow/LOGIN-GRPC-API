# LOGIN-GRPC-API
Repository for practical work on GRPC.
This repository also proposes the REST servers and requests described at the end of this README, in the "REST REQUESTS" part.

### Installation

First clone this repo with `git clone https://github.com/Mashbrow/LOGIN-GRPC-API`
To launch with docker-compose, get to the LOGIN-GRPC-API folder and type `docker-compose up` in your terminal. Then use the requests of the REST servicies.

### What was done so far

  - Green Practical Work done completely.
    - Folders `user` and `booking` correspond to this version.
  - Blue Practical Work done completely:
    - The blue version of booking is in the folder `booking-grpc`, files `users2` and `booking_grpc`correspond to the blue version
  - Red Practical Work done completely:
    - The red version of booking can be found in the folder `client` under the name of `client_booking_asynchronous`.

## Client
Folder that contains the clients corresponding to the servers described in the following sections.
To test a client, first launch the corresponding server, and then launch the client.

"client.py" is the client for the movie service. It requires the following servers to be launched:  
- movie

"client_booking.py" is the client for the booking service. It requires the following servers to be launched:  
- booking  
- showtime  

"client_booking_asynchronous.py" is the client for the booking service. It works asynchronously. It requires the following servers to be launched:
- booking  
- showtime
Note: Nothing has to be done server side, it completely depends on the client to make the connection asynchronous.

"client_showtime.py" is the client for the showtime service. It requires the following servers to be launched:  
- showtime  

###### EXCEPTION : the user client
The user client is in REST so to be used with http requests. The following GRPC servers are required to be launched:  
- user  
- movie
- showtime
  
In addition, the REST serveur booking is required to be launched.     

## User
Folder containing the user server. Execute the user.py file to launch the server.

## Movie
Folder containing the movie server. Execute the movie.py file to launch the server.

## Booking
Folder containing the booking server. Execute the booking_grpc.py file to launch the server.  
NOTE: the booking folder also contains a booking.py file that dosesn't launch the grpc server. It is in fact the REST version of booking.

## Showtime
Folder containing the showtime server. Execute the showtime.py file to launch the server.


# REST REQUESTS
## BOOKING

Port:3003  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/booking": returns the booking database as a json.  
"/booking/&lt;userid&gt;": returns the bookings for a particular user as a json.  

Posts:  
"booking/&lt;userid&gt;": takes a booking as request, adds a booking for the user.  


## USER
Port:3004  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/user": returns the user database as a json.  
"/user/&lt;userid&gt;": returns the average rating for that user.

## USER2
Port:3006  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/user": returns the user database as a json.  
"/user/&lt;userid&gt;": returns the average rating for that user.
