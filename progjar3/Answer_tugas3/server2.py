import socket

UDP_IP_ADDRESS = '192.168.122.14'
UDP_PORT = 5050

serverSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSock.bind(((UDP_IP_ADDRESS,UDP_PORT)))
filename='server2.jpg'
fp = open(filename,'wb+')
wrt=0
count=0
while True:
    data, addr = serverSock.recvfrom(1024)
    cnt=cnt+len(data)
    print(addr," blok ", cnt,"panjang : ",len(data), data)
    fp.write(data)