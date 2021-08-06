# you can use this to connect to the server socket in socket_server.py

import socket  # imports the socket module so we can connect to the server


def get_text(receiving_socket):  # a function to receive the message
    buffer = ""  # this buffer is used to append the message to it as it is received

    socket_open = True  # sets up the while loop
    while socket_open:
        # read any data from the socket
        data = receiving_socket.recv(1024)  # gets the receiving socket (server_socket) and calls the built in recv
        # function to receive 1024 bytes of data, which is the maximum amount of data that can be received

        # if no data is returned the socket must be closed
        if not data:
            socket_open = False  # stops the while loop

        # add the data to the buffer
        buffer = buffer + data.decode()  # adds the decoded data through UTF-8 to the buffer string variable

        # is there a terminator in the buffer
        terminator_pos = buffer.find("\n")  # uses python's built in function to find the terminating character '\n'
        # if the value is greater than -1, a \n must exist
        while terminator_pos > -1:  # if string.find() returns -1, '\n' could # not be found
            # get the message from the buffer
            message = buffer[:terminator_pos]
            # remove the message from the buffer
            buffer = buffer[terminator_pos + 1:]  # takes off the \n
            # yield the messages, like return
            yield message  # yield is used to return certain kinds of functions, generators
            # is there another terminator in the buffer
            terminator_pos = buffer.find("\n")
        socket_open = False


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # sets up a socket with ip and TCP, the same as
# the server one
client_socket.connect(("127.0.0.1", 8081))  # connects to the ip and port of the server
print("Connected")

"""
data = client_socket.recv(1024)  # data is received and added to the data variable
# The value 1024 is the maximum number of bytes that should be read at one time. If more than 1,024 bytes had been
# sent, subsequent calls to recv would receive the rest of the data.
message = data.decode()  # decodes the message
print(message)  # prints the message
"""

print('Message received:\n ')
for message in get_text(client_socket):  # prints the message using the get_text function
    print(message)

"""
you could also use next to call get_text once and get a single message:

message = next(get_text(client_socket))
print(message)

"""

""" sends a message back to the server:
message = "message received"
data = message.encode()
client_socket.send(data)
"""
client_socket.close()  # it is good practice to close sockets
