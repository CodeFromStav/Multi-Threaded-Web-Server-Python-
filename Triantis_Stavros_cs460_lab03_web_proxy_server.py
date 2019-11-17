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
   print("Socket binded to port ", PORT + "\n")
   #API: listen()
   s.listen()
   print("Socket is listening... \n")

   #Connection
   connection_socket, client_address = server_socket.accept()
   p = threading.Thread(name = str(client_address), target = http_handler, args = (connection_socket, client_address))
   
   p.setDaemon(True)
   p.start()

   #API: connect()
   conn, addr = s.accept() #passing to accept
   print("Accepted address \n")

   with conn:
      print('Connected by ', addr)
      #API: recv()
      while True: 
         #Handle service request (request for information/something)


         data = conn.recv(1024)
         if not data: #if no data sent
            break
         #API: send()
         conn.sendall(data)
      s.close()
         
      #handles concurrent requests by forking a process for each new client request
def http_handler(connection_socket, client_address): #nested function to check valid request line

         req_lines = request.splitlines()
         req_lines = req_lines[0].split(" ")

         METHOD = req_lines[0] 
         URL = req_lines[1]
         VERSION = req_lines[2] 
                                
         request = ["GET", "POST", "HEAD", "PUT", "PATCH", "DELETE"]
         version = ["HTTP/1.0", "HTTP/1.1"]
         response = "HTTP/1.1 2-- OK\r\nHost: localhost\r\n<!DOCTYPE html><body><h1>Simple Web Server</h1><p>I love computer networks!</p></body></html>/r/n"
        
         if ( METHOD == request[1] or METHOD == request[2] or METHOD == request[3] or METHOD == request[4] or METHOD == request[5] ):         
                  return "501, Not Implemented "
         
         elif( URL == "/" and VERSION == version[0] ):
                  return response

         elif( URL == "/" and VERSION == version[1] ):
                  return "200, Success "                                                                        
                                                                           
         else:
                  return "404 Not Found "
                                    
                                    
         if ( len(request) == 3 ):
                  pass
         else:
                  return "400 Bad Request "





      #Create Child Process(Fork)
      #   if __name__ == "__main__":
                
      #           p1 = multiprocessing.Process( target = http_handler, args = request ) #fill in process
      #           p2 = multiprocessing.Process( target = http_handler, args = request ) #target = [functionname], args = ( [functionarguement])

      #           p1.start() #starts
      #           p2.start()

      #           p1.join() #wait until prior process finished
      #           p2.join()
            

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

                     


#Close
#API: close()
