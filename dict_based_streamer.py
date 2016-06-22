__author__ = 'barrycahill'

import socket
import netifaces as ni
import struct

ni.ifaddresses('en0')
UDP_IP = ni.ifaddresses('en0')[2][0]['addr']
#This will automatically now get the best
UDP_PORT = 5001
buffer_size = 110   # buffer size is 110 bytes

print 'Current using IP address: ',  UDP_IP, 'Port : ', UDP_PORT
sock = socket.socket(socket.AF_INET,   # Internet
                     socket.SOCK_DGRAM)    # UDP
sock.bind((UDP_IP, UDP_PORT))

xdata = [0]
while len(xdata) < 10:
    data, addr = sock.recvfrom(buffer_size)
    # print "received message:", data
    x_axis = struct.unpack('f', data[4:8])
    #data unpacked for the accelerometer

    x_axisrd = "%.2f" % x_axis
    xdata.append(x_axisrd)
    # data rounded off so we can detect 'major' movement
    print xdata
# it's now showing a fairly long string
sock.shutdown()
sock.close()