This program

README with a description of what the program does, how to compile (if necessary), how to run, and what to expect as output.

This program is a Web server capable of accepting HTTP requests and returning response data to a client.
In order to you use, type "python sst46_webserver.py --port 2080". Open a new shell and type telnet localhost 2080.
Finaly type in "GET / HTTP/1.0 or GET / HTTP/1.1". 

You will either get an output of the response with 1.1, or a 200 success with 1.0.
