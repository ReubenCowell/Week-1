import socket  # to use the socket api, import the module


def send_text(sending_socket, text):  # this adds a terminating character to the string and sends
    text = text + "\n"  # appends the "\n" terminating character to the string
    data = text.encode()  # encodes the string using UTF-8
    sending_socket.send(data)  # sends the string using the built in function for sending data


message = input('what do you want to send?')  # gets the message that is to be sent to the client
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a socket
# the parameter AF_INET is to use ip and SOCK_STREAM tells it to use TCP

server_socket.bind(("0.0.0.0", 8081))  # binds the socket to a ip, 0.0.0.0 and the port 8081 as it is used for testing
server_socket.listen(0)  # tells it to listen for a connection to be made
print("Waiting for connection")

connection_socket, address = server_socket.accept()  # if you put 127.0.0.1:8081 into a web browser, it will not
# display anything, but this will be seen as connected,  172.0.0.1  is the local port of this computer
"""
socket.accept()
Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair (conn, address) where conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.

The newly created socket is non-inheritable."""
print("connected")

"""Ports are typically used to identify the purpose of the connection and can be any number between 0 and 65535. 
Ports 0 to 1023 are well known ports that are usually restricted for specific uses: for example, port 80 is HTTP and 
should not really be used. """

send_text(connection_socket, message)  # calls the send function that also adds a end of transmission character

""" this works, it receives a message back from the client
msg = connection_socket.recv(1024)
message = msg.decode()
print(message)
"""

# it is good practice to close the sockets:
connection_socket.close()
server_socket.close()
