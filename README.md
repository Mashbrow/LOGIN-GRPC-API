# LOGIN-GRPC-API
Repository for practical work on GRPC.
This repository also proposes the REST servers and requests described at the end of this README, in the "REST REQUESTS" part.  
To launch with docker-compose, get to the LOGIN-GRPC-API folder and type `docker-compose up` in your terminal. Then use the requests of the REST servicies.  

  - TP vert effectué.
    - Les dossiers user et booking correspondent à la version du tp vert.
  - TP bleu effectué:
    - La version du TP bleu de booking est dans le dossier `booking-grpc`. Les dossiers user2 et booking_grpc correspondent à la version du tp bleu.
  - TP rouge effectué:
    - La version du TP rouge de booking est dans le dossier `client` sous le nom `client_booking_asynchronous`.

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

Port:3201  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/booking": returns the booking database as a json.  
"/booking/<userid>": returns the bookings for a particular user as a json.  

Posts:  
"booking/<userid>": takes a booking as request, adds a booking for the user.  

## MOVIE
Port:3200  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/template": returns the homepage following a template.  
"/json":returns the movie database as a json.  
"/movie/<movieid>": returns the data for a particular movie as a json.  
"/moviebytitle": takes a movie title as request, returns the data for this particular movie as a json.  

Posts:  
"/movie/<movieid>": takes a movie as request, adds a movie to the database.  

Puts:   
"/movie/<movieid>/<rate>": changes the rating for a given movie.  

## SHOWTIME 
Port:3202  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/showtime": returns the showtime database as a json.  
"/showtime/<date>": returns the shows for a particular date as a json.  

## USER
Port:3203  
Host: localhost  
Gets:   
"/": returns the homepage.  
"/user": returns the user database as a json.  
"/user/<userid>": returns the user with this id as a json.  
