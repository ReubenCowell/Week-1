import socket  # to use the socket api, import the module


def send_text(sending_socket, text):  # this adds a terminating character to the string and sends
    text = text + "\n"
    data = text.encode()
    sending_socket.send(data)


message = input('what do you want to send?')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a socket

# AF_INET to use ip and SOCK_STREAM tells it to use TCP
server_socket.bind(("0.0.0.0", 8081))  # binds the socket to a ip, 0.0.0.0 and the port 8081 as it is used for testing
server_socket.listen()  # tells it to listen for a connection to be made
print("Waiting for connection")
connection_socket, address = server_socket.accept()  # if you put 127.0.0.0:8081 into a web browser,
"""Ports are typically used to identify the purpose of the connection and can be any number between 0 and 65535. 
Ports 0 to 1023 are well known ports that are usually restricted for specific uses: for example, port 80 is HTTP and 
should not really be used. """
# it appears as connected, 17.0.0.0 is the local port of this computer
print('connected')

send_text(connection_socket, message)  # calls the send function that also adds a end of transmission character

msg = connection_socket.recv(1024)
message = msg.decode()
print(message)

# it is good practice to close sockets:
connection_socket.close()
server_socket.close()
