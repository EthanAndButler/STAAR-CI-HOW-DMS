#!/usr/bin/env python
# coding: utf-8

# # Single message

# In[ ]:


import socket

# set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('localhost', 5000)) # choose any port number you like
server_socket.bind(('192.168.137.7', 5000)) # choose any port number you like
server_socket.listen(1) # listen for one client connection

print('Waiting for client connection...')

# accept a client connection
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

# receive data from the client
data = client_socket.recv(1024) # receive up to 1024 bytes
print('Received message:', data.decode())

# close the sockets
client_socket.close()
server_socket.close()


# # Stream

# In[ ]:


import socket
import time

# set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.137.7', 5000)) # choose any port number you like
server_socket.listen(1) # listen for one client connection

print('Waiting for client connection...')

# accept a client connection
client_socket, client_address = server_socket.accept()
print('Connected by', client_address)

while True:
    # get the current date and time
    data = client_socket.recv(1024)
    if data:
        print('Received message:', data.decode())

    # send the data to the client
    # client_socket.sendall(data)

    # wait for one second
    time.sleep(1)

# close the sockets
client_socket.close()
server_socket.close()


# # Echo server

# In[23]:


import socket
import time

HOST = "192.162.0.228"
HOST = "0.0.0.0"
PORT = 65432

counter = 0
# set up the server socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT)) # choose any port number you like
    s.listen() # listen for one client connection

    while counter < 1000:
        conn, addr = s.accept()

        with conn:
            # print(f"Connected by {addr}")
            while True:
                # get the current date and time
                data = conn.recv(1024)
                if data:
                    counter += 1
                    print(f'{data.decode()}')
                    message = b"Message received"
                    # conn.sendall(message)
                    # conn.close()
                    break
                # wait for one second
        time.sleep(1)

