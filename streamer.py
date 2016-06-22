__author__ = 'barrycahill'

import struct
import socket
import sys

print sys.stdout.encoding

UDP_IP = "192.168.1.17"
UDP_PORT = 5006
buffer_size = 110   # buffer size is 110 bytes

sock = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)    # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(buffer_size)
    # print "received message:", data
    # x_accel = unpack('f', data[4:7])
    # print x_accel
    # x_acc = data[4:7]
    # value = struct.unpack('f',x_acc)
    x_acc = struct.unpack('i',data[4:8])
    print x_acc


