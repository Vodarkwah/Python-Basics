# MAKING AN HTTP REQUEST IN PYTHON

import socket
# Sending request

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()    #   SENDS HTTP REQUEST
mysock.send(cmd)                                            #   encode prepares the data to go across the internet

# Receiving Request
while True:
    data = mysock.recv(512) # receive 512 char
    if (len(data) < 1): # Closes if str is 0. i.e. marks the end of the line
        break
    print(data.decode(),end='')  # decodes the sent file
mysock.close() # closes socket

#tracebak if no internet connection