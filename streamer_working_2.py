__author__ = 'barrycahill'

import socket
import netifaces as ni

ni.ifaddresses('en0')
UDP_IP = ni.ifaddresses('en0')[2][0]['addr']
#This will automatically now get the right address
UDP_PORT = 5006
buffer_size = 110   # buffer size is 110 bytes

print 'Current listening on the following IP address: ',  UDP_IP, 'Port : ', UDP_PORT
print 'Set up the streamer app with the same details'

sock = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)    # UDP
sock.bind((UDP_IP, UDP_PORT))
# initiate the UDP socket / listening

while True:
    data, addr = sock.recvfrom(buffer_size)
    print "received message:", data

# print the data
# how to translate to something meaningful