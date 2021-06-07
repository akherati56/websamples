#!/usr/bin/env python3

# Importing socket library
import socket
from config import PORT , ServerIp

# Now we can create socket object
s = socket.socket()

# Lets choose one port and start listening on that port

print("\n Server is listing on port :", PORT, "\n")

# Now we need to bind to the above port at server side
s.bind(('172.20.10.4', PORT))

# Now we will put server into listenig  mode
s.listen(10)

#Open one recv.txt file in write mode
file = open("recv.txt", "wb")
print("\n Copied file name will be recv.txt at server side\n")

# Now we do not know when client will concatct server so server should be listening contineously
while True:
    # Now we can establish connection with clien
    conn, addr = s.accept()

    # Send a hello message to client
    msg = "\n\n|---------------------------------|\n Hi Client[IP address: "+ addr[0] + "], \n ֲֳ**Welcome to Server** \n -Server\n|---------------------------------|\n \n\n"
    conn.send(msg.encode())

    # Receive any data from client side
    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    # Close the file opened at server side once copy is completed
    file.close()
    print("\n File has been copied successfully \n")

    # Close connection with client
    conn.close()
    print("\n Server closed the connection \n")

    # Come out from the infinite while loop as the file has been copied from client.
    break
