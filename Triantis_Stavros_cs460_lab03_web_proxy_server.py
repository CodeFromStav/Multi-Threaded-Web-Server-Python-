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



         
         
         data = conn.recv(1024)
         if not data: #if no data sent
            break
         #API: send()
         conn.sendall(data)
      s.close()
                      


#Close
#API: close()
