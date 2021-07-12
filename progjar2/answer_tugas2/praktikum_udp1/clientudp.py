import socket
import time

TARGET_IP = "192.168.122.220"
TARGET_PORT = 5003

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
number = 0
while True:
    number = number+1
    msg = " Showing Number - {} " . format(number)
    print(msg)
    sck.sendto(msg.encode(), (TARGET_IP, TARGET_PORT))
    time.sleep(1)