import sys
import socket
import string
import random

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.122.244', 10000) #alpine 1
server_address2 = ('192.168.122.136', 10000) #alpine 2
print(f"connecting to alpine 1 {server_address}")
print(f"connecting to alpine 2 {server_address2}")
sock.connect(server_address)
sock2.connect(server_address2)


try:
    # Send data
    message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    message2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(2000000))
    print(f"sending to alpine 1 {message}")
    print(f"sending to alpine 2 {message2}")
    sock.sendall(message.encode())
    sock2.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(250)
        amount_received += len(data)
        print(f"{data}")
    amount_received2 = 0
    amount_expected2 = len(message)    
    while amount_received2 < amount_expected2:
        data2 = sock2.recv(250)
        amount_received2 += len(data2)
        print(f"{data2}")
finally:
    print("closing")
    sock.close()
    sock2.close()
