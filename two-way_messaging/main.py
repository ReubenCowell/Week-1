import socket  # we need the socket library so we can send messages over a network

user = input('Would you like to be the server (1) or client (2)? \n>')  # asks the user whether they are a server or
# client


def reply():  # the code to receive and reply to messages
    message = client_socket.recv(1024).decode()  # receives a message from the client and decodes it
    print("Message received:\n\n'"+message+"'\n")  # displays the message to the user
    reply = input("Your reply >>>").encode()  # gets and encodes a reply
    client_socket.send(reply)  # sends the reply to the client
    print('Waiting for reply...\n')


if user == '1':  # if the user is the server:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creates a server socket object using ip and tcp
    server_socket.bind(("0.0.0.0", 8081))  # binds the socket to an ip and tcp
    server_socket.listen()  # tells it to listen for a connection to be made to the server
    client_socket, address = server_socket.accept()  # creates new socket object as client_socket
    print("Connection detected at... " + str(address))  # shows where the connection is from
    reply_1 = client_socket.recv(1024)  # receives the initial message
    print(reply_1.decode())  # decodes and prints it to the user
    client_socket.send("Connected to server \n\n".encode())  # sends an initial message

elif user == '2':  # if the user is the client:
    connect_ip = input("What ip address would you like to connect to?")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # once again, sets up a ip/tcp socket, stream
    client_socket.connect((connect_ip, 8081))  # connects the socket to the ip that the user wants to connect to
    client_socket.send("Connected to client\n\n".encode())  # the initial message to the server
while True:
    reply()  # calls the function that reads and lets you reply to messages
