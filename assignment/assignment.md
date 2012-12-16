## Project Description
Write a simple HTTP server capable of serving GET requests for static content using sockets in Python 3. For testing, files should be stored in a `www` directory relative to `server.py`. Follow RFC 2616 for the portion you need to implement. 

You should use the python [sockets library](http://docs.python.org/3/library/socket.html) to listen for requests on a port. Basically, you need to wait for a GET request, respond with the appropriate file, and then close the connection. Do not use any web server libraries, as the point of the assignment is to implement it from scratch.

There should also be a configuration file (`server.conf`) which stores at least the following data:
* Port to listen on
* Directory (relative or absolute path)
* Default webpage(s) (i.e. which will be given if someone sends a `GET /` request)

You will also need to handle exceptions for at least a 404 (file not found) error by responding appropriately according to the RFC. 

For debugging, netcat, telnet, lynx, and tcpdump may be useful. Here is an [example](http://www.d.umn.edu/~gshute/net/http-script.html) of debugging HTTP over telnet.


## Grading Criteria
* 60 points - functionality
** 10 points - the program listens on the port specified in `server.conf` for HTTP requests
** 20 points - the program responds with the contents of the appropriate file when a valid GET request is recieved
** 10 points - content is served according to the directory structure
** 10 points - exceptions are properly used (rather than if-statements for everything)
** 10 points - 404 errors are handled
* 40 points - code style
** 10 points - relevent config data is stored in a separate file rather than hard-coded
** 20 points - the code is modular and separated into different functions, files, and classes as appropriate 
** 10 points - the program is well documented and the code is commented
* 10 points - Extra credit: make it multithreaded so it supports multiple connections at once

## Useful Documentation
* [RFC 2616: Hypertext Transfer Protocol](http://www.w3.org/Protocols/rfc2616/rfc2616.html)
* [HTTP over telnet](http://www.d.umn.edu/~gshute/net/http-script.html)
