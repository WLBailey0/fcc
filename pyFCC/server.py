import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = 192.168.0.197
host = socket.gethostname()
port = 4444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientSocket, address = serversocket.accept()
    print('Recieved connection from %s' % str(address))

    message = 'Thank you for connection to the server' + '\r\n'

    clientSocket.send(message.encode('ascii'))

    

    clientSocket.close()

