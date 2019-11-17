#!/usr/bin/env python3

import argparse
import sys
import itertools
import socket
import argparse
import threading
import multiprocessing
from multiprocessing import Pool
# import importlib

# moduleName = input('Lab03Pre.py')
# importlib.import_module(Lab03Pre.py)

from socket import socket as Socket

# A simple web server

# Issues:
# Ignores CRLF requirement
# Header must be < 1024 bytes
# ...
# probabaly loads more

def main():
        # Command line arguments. Use a port > 1024 by default so that we can run
        # without sudo, for use as a real server you need to use port 80.
        parser = argparse.ArgumentParser()
        parser.add_argument('--port', '-p', default=2080, type=int, help='Port to use')
        args = parser.parse_args()

        # Create the server socket (to handle tcp requests using ipv4), make sure
        # it is always closed by using with statement.
        with Socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

        # The socket stays connected even after this script ends. So in order
        # to allow the immediate reuse of the socket (so that we can kill and
        # re-run the server while debugging) we set the following option. This
        # is potentially dangerous in real code: in rare cases you may get junk
        # data arriving at the socket.

                # Set socket options
                server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

                # Bind socket to port
                server_socket.bind(('', args.port))

                # Have socket listen
                server_socket.listen(0)

                print("server ready")

                while True:
                
                # Use the server socket as the connection socket and accept incoming requests
                # This is like file IO and you need to open the server socket 
                # as the connection socket
                        with server_socket.accept()[0] as connection_socket:
                        
                                # Save the request received from the connection and decode as ascii
                                data_str = connection_socket.recv(1024).decode('ascii')
                                request = data_str
                                reply = http_handler(request)
                                connection_socket.send(str.encode(reply))
                                
                                print("\n\nReceived request")
                                print("======================")
                                print(request.rstrip())
                                print("======================")
                                print("\n\nReplied with")
                                print("======================")
                                print(reply.rstrip())
                                print("======================")
                                
def http_handler(request):
                        
        req_lines = request.splitlines()
        req_lines = req_lines[0].split(" ")


        METHOD = req_lines[0] 
        URL = req_lines[1]
        VERSION = req_lines[2] 
                                
        request = ["GET", "POST", "HEAD", "PUT", "PATCH", "DELETE"]
        version = ["HTTP/1.0", "HTTP/1.1"]
        response = "HTTP/1.1 2-- OK\r\nHost: localhost\r\n<!DOCTYPE html><body><h1>Simple Web Server</h1><p>I love computer networks!</p></body></html>/r/n"
        if ( METHOD == request[1] or METHOD == request[2] or METHOD == request[3] or METHOD == request[4] or METHOD == request[5] ):         
                return "501, Not Implemented_TESSTT "
        
        elif( URL == "/" and VERSION == version[0] ):
                return response

        elif( URL == "/" and VERSION == version[1] ):
                return "200, Success "                                                                        
                                                                        
        else:
                return "404 Not FoundDD"
                                 
       	                        
        if ( len(request) == 3 ):
                pass
        else:
                return "400 Bad Request"
                                        
                                        
                        
if __name__ == "__main__":
        sys.exit(main())
        
        
 # Generate a reply by sending the request received to http_handle()
	    	                #CS460_TODO
                      
                                
                                 #Step 1: EXTRACT THE REQUEST LINE
                                 #1a: Split up the request string by line (/r/n) --> ASSUME:
                                 #  LIST of LINES   
                                 
                                 #1b: Request Line is going to be at index position 0
                                 #  in our lines from step 1a --> Assume: string called req_line
                                 
                                 
                                 #Step 2: Extracting the METHOD, URL, and VERSION fields from
                                 #  the Request Line
                                 #2a: Split req_line on spaces --> ASSUME: List of fields
                                 
                                
                                 
                                 #2ba: Check the length of list of fields to see if it is 3
                                 # ...if not GENERATE ERROR CODE
                                       
                                 #2b: METHOD is going to be at index position 0
                                 #2c: URL is going to be at index position 1
                                 #2d: VERSION is at index position 2 (valid versions are 1.0 & 1.1)
                                          
                                 #Step 3: If the values in the Request line are valid,
                                 #  we proceed to check that headers are correctly formatted
                                 #3a: Check to see if METHOD is [GET, POST, HED, PUT, PATCH, DELETE]:
                                 #  If it is not --> GENERATE ERROR CODE 
                                 
                                #  if METHOD == "GET" or METHOD == "POST" or METHOD == "HEAD" or METHOD == "PUT" or METHOD == "PATCH" or METHOD == "DELETE":
                                 
                                #          #3b: Check to see if VERSION is [HTTP/1.1, HTTP/1.0]:
                                 
                                #          if ( VERSION = "HTTP/1.1" or VERSION = "HTTP/1.0"):
                                         
                                                 
                                         
                                #      #  If it is not--> GENERATE ERROR CODE

                                #          else: 
                                #          print( GENERATE_ERROR_CODE );
                                         
                                         
                                 
                
                                 
                                 
                                 
                             #***OPTIONAL   #3c: Check out headers to make sure they are in
                             #  "key: value" format
                                 #3d: If METHOD is not GET, GENERATE ERROR CODE, otherwise,
                                 #  keep going forward
                                 
                                 #Step 4: Check if the requested file is available or not
                                 #4a: Check to see if the file exists... If it does not -->
                                 #  GENERATE ERROR CODE (404)
                                         
        
                                 #Step 5: Send the response
                                 #5a: If an error code was generated, send the error code
                                 #5b: If no error code was generated, serve the default HTML
                                 
                                 

		                # Use the connection socket to send the reply encoded as bytestream
		                #CS460_TODO