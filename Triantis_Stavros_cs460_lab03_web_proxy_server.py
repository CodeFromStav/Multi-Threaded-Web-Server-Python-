#Server program that echos any message that is sent
import socket
import multiprocessing
from multiprocessing import Pool

HOST = '127.0.0.1' #local host IP
PORT = 2080 #Generall use any large number > 1023

#Setup
#API: socket()
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #socket(IPV4_Flag, TCP_Flag)


   #API: bind()
   s.bind((HOST, PORT))
   #API: listen()
   s.listen()

   #Connection
   #API: connect()
   conn, addr = s.accept() #passing to accept
   with conn:
      printf('Connected by ', addr)
      #API: recv()
      while True: 
         #Handle service request

         #Create Child Process(Fork)
            

         #Read data from client, ensure recieve request containing valid request line:
            #<METHOD><URL><HTTP VERSION>
            #ex: GET http://www.cs.princeton.edu/index.html HTTP/1.0
         
         #Check Header Format:
            #<HEADER NAME>:<HEADER VALUE>


         #If request is invalid from client, output "Bad Request" (400)

         #If request has valid HTTP method but not a <METHOD> (GET), output "Not Implemented" (501)

         #If headers not properly formatted for parsing, output type-400 message

         
         
         
   #Create function that parses HTTP Requests to ensure they have a valid request line
      #{

      #If request is invalid from client, output "Bad Request" (400)

      #If request has valid HTTP method but not a <METHOD> (GET), output "Not Implemented" (501)

      #If headers not properly formatted for parsing, output type-400 message
      #}

   #Once proxy recieves valid HTTP Request (after parsed), need to parse requested URL
      #must be host, port, path

         #if hostname in URL does not have port specified, default HTTP port to 80


   #If response received, return response message as-is to client via appropriate socket



         
         
         data = conn.recv(1024)
         if not data: #if no data sent
            break
         #API: send()
         conn.sendall(data)
      s.close()
                      


#Close
#API: close()
