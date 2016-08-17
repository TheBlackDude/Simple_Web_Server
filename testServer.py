import socket

HOST, PORT = '', 8888

# create the socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket
listen_socket.bind((HOST, PORT))
# listen for connections
listen_socket.listen(1)
print('Serving HTTP on port {0} ...'.format(PORT))

while True:
    # get client imformation
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print(request)

    http_response = """ HTTP/1.1 200 OK Hello, world! """
    client_connection.sendall(bytes(http_response, 'utf-8'))
    client_connection.close()
