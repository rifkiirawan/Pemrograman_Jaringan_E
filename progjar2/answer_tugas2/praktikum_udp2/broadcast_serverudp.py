import socket

SERVER_IP = '192.168.1.1'
SERVER_PORT = 5003

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sck.bind(("", SERVER_PORT))

while True:
    data, addr = sck.recvfrom(1024)
    print(addr)
    print("Recieved ", data)
    print("Sent By : " , addr)