import sys
import socket

# Create a TCP/IP socket
socket_alpine1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_alpine2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
address_alpine_1 = ('192.168.122.244', 10000)
address_alpine_2 = ('192.168.122.136', 10000)
print(f"connecting to alpine 1 {address_alpine_1}")
print(f"connecting to alpine 2 {address_alpine_2}")
socket_alpine1.connect(address_alpine_1)
socket_alpine2.connect(address_alpine_2)


try:
    # Send data image
    message = open("one-punch-man-ok-rs.jpg", 'rb')
    message_read = message.read()
    print(f"sending {message}")
    socket_alpine1.sendall(message_read)
    socket_alpine2.sendall(message_read)

    # Look for the response alpine 1
    amount_received_1 = 0
    amount_expected_1 = len(message_read)
    file_1 = bytearray()
    while amount_received_1 < amount_expected_1:
        data_1 = socket_alpine1.recv(16)
        amount_received_1 += len(data_1)
        file_1 += data_1
        print("from alpine 1: ", f"{data_1}")
    
    # write file respon dari alpine 1
    write_1 = open("saitama_alpine1.jpg", 'wb')
    write_1.write(file_1)
    write_1.close()

    # Look for the response alpine 2
    amount_received_2 = 0
    amount_expected_2 = len(message_read)
    file_2 = bytearray()
    while amount_received_2 < amount_expected_2:
        data_2 = socket_alpine2.recv(16)
        amount_received_2 += len(data_2)
        file_2 += data_2
        print("from alpine 2: ", f"{data_2}")

    # write file respon dari alpine 2
    write_2 = open("saitama_alpine2.jpg", 'wb')
    write_2.write(file_2)
    write_2.close()
finally:
    print("closing")
    socket_alpine1.close()
    socket_alpine2.close()