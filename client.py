#!/usr/bin/env python
# coding: utf-8

# In[16]:


import socket

# set up the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000)) # connect to the server on port 5000

# send a message to the server
message = 'asdas!'
client_socket.sendall(message.encode())


# In[22]:


message = 'Hi'
client_socket.sendall(message.encode())


# In[ ]:



# close the socket
# client_socket.close()

