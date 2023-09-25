#import socket module
from socket import *
import sys # In order to terminate the program


serverSocket = socket(AF_INET , SOCK_STREAM)
# Prepare a server socket on a particular port # Fill in code to set up the port
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("listening on port", serverPort)

while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()# Fill in code to get a connection
    
    try:
        message =  connectionSocket.recv(6789).decode()# Fill in code to read GET request 
        filename = message.split()[1]
        print(filename[1:])
        
        # Fill in security code
        if(filename[1:] == "grades" or filename[1:] == "grades/students.html"):
            connectionSocket.send("HTTP/1.1 403 Forbidden\r\n\r\n".encode())
            

        else:
            f = open(filename[1:])
            outputdata = f.read() # Fill in code to read data from the file 
            f.close()

            # Send HTTP header line(s) into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

            # Send the content of the requested file to the client for i in range(0, len(outputdata)):
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            

            connectionSocket.send("\r\n".encode())
            connectionSocket.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        # Close client socket
        connectionSocket.close()
  
serverSocket.close()
sys.exit() # Terminate the program after sending the corresponding data