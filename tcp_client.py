import socket, sys
port = 9999
    
if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((sys.argv[1], port))
    server.send(b'GET / HTTP/1.1\nHost:localhost\n')

    print(server.recv(4096))