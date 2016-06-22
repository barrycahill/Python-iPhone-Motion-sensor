import netifaces as ni
ni.ifaddresses('en0')
ip = ni.ifaddresses('en0')[2][0]['addr']
print ip
# this one is working now