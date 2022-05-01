**CS 4390.002 Web Proxy Project
Group#: 12
Date: April 30, 2022
Team Leader: David Teran (DXT180025)
Team Members: Duy Vu (DKV180001)**

This is the Web Proxy Project for CS 4390.002. This project uses Python as the main programming language
and requires a web browser of the user's choice in order for the program to function correctly. Project
will take in a host, port, and website link of choice that is entered in the web browser and will print
out the HTTP request and response messages as well as the headers included in the request and response.
Program will also return an HTTP response status and will write the file into the cache. Program will also
check if the given file is found in cache memory. If the file is found in cache memory, program wil retrieve
and print out the file from cache memory. Otherwise, it will send an HTTP request to the original server.

How to Use:
1. Start the web proxy server. A message should appear if the program started up correctly:
   "HTTP Proxy Server is listening on IP and port: <USERHOST>(or localhost):<USERPORT>"
2. On the web browser of choice, open up a new tab and enter the following on the search bar
   http://<USERHOST>(or localhost):<USERPORT>/<WebSite>
3. Browser should then display the requested page while the terminal prints out the information
   from the request and the response as well as check if the objects requested were in cache or not.
4. Once done, either press 'X' to close the server or press enter to do another request. In doing
   another request, close the previous tab and open another new tab and repeat the process.
