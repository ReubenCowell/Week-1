# you can use this to connect to the server socket in socket_server.py

import socket  # imports the socket module


def get_text(receiving_socket):  # to receive the message
    buffer = ""

    socket_open = True
    while socket_open:
        # read any data from the socket
        data = receiving_socket.recv(1024)

        # if no data is returned the socket must be closed
        if not data:
            socket_open = False

        # add the data to the buffer
        buffer = buffer + data.decode()

        # is there a terminator in the buffer
        terminator_pos = buffer.find("\n")
        # if the value is greater than -1, a \n must exist
        while terminator_pos > -1:
            # get the message from the buffer
            message = buffer[:terminator_pos]
            # remove the message from the buffer
            buffer = buffer[terminator_pos + 1:]
            # yield the message (see below)
            yield message
            # is there another terminator in the buffer
            terminator_pos = buffer.find("\n")


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # sets up a socket with ip and TCP, the same as
# the server one
client_socket.connect(("127.0.0.1", 8081))  # connects to the ip and port
print("Connected")

"""
data = client_socket.recv(1024)  # data is received and added to the data variable
# The value 1024 is the maximum number of bytes that should be read at one time. If more than 1,024 bytes had been
# sent, subsequent calls to recv would receive the rest of the data.
message = data.decode()  # decodes the message
print(message)  # prints the message
"""
for message in get_text(client_socket):
    print(message)

message = "message received"
data = message.encode()
client_socket.send(data)

client_socket.close()  # it is good practice to close sockets
