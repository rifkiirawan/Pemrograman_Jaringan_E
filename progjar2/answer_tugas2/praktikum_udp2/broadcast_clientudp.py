import socket
import time

TARGET_IP = '192.168.122.250'
TARGET_PORT = 5003

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sck.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

number = 0
while True:
    number = number+1
    msg = " BROADCAST - Showing Number - {} " . format(number)
    print(msg)
    sck.sendto(msg.encode(), ("255.255.255.255", TARGET_PORT))
    time.sleep(1)