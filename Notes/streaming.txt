https://www.futurelearn.com/courses/networking-with-python-socket-programming-for-communication/6/steps/1120262
Streaming:

The TCP protocol streams data over a connection. The socket functions send and recv suggest that individual messages are sent and received. This, however, is not true.

every time a socket sends a message, a lot of bytes are sent, called a stream

TCP makes sure that all bytes in the stream will arrive to the socket in the corrcect order
There is, however, no guarantee that the number of bytes returned by a call to recv will be the same number of bytes sent using send.

It could be that multiple messages have been sent using send, which are retrieved by a single call to recv.

there may have to also be multiple rcv to retrive all the bytes in a message
This creates two practical problems for programmers:

1. How to determine the end of one message and the start of another
2. How to reconstruct a single message from multiple sets of bytes

when there is only text in a message, you can add an end of transmisssion message like \n or \4
