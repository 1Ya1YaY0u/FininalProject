import socket


class Client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostIP = '127.0.0.1'
        self.hostPort = 62201

    def startClient(self):
        self.sock.connect((self.hostIP, self.hostPort))
        recvInfo = self.sock.recv(1024)     # recv tips from server
        print(recvInfo.decode('utf-8'))
        passwd = input()    # input passwd
        self.sock.send(passwd.encode('utf-8'))  # send passwd to server
        result = self.sock.recv(64).decode('utf-8')     # recv result from server
        print(result)


if __name__ == "__main__":
    client = Client()
    client.startClient()
