__author__ = 'barrycahill'

import socket

UDP_IP = "192.168.1.17"    #replace with current IP from settings
UDP_PORT = 5006
buffer_size = 110   # buffer size is 110 bytes

sock = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)    # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(buffer_size)
    print "received message:", data