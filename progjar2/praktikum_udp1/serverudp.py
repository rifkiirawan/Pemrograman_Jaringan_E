import socket

SERVER_IP = '192.168.122.220'
SERVER_PORT = 5003

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.bind((SERVER_IP, SERVER_PORT))

while True:
    data, addr = sck.recvfrom(1024)
    print("Recieved ", data)
    print("Sent by : " , addr)