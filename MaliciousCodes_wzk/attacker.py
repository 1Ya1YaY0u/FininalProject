import socket


class Server(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.hostIp = '127.0.0.1'
        self.hostPort = 9999
        self.clientIp = '127.0.0.1'
        self.clientPort = 9998

    def main(self):
        self.sock.bind((self.hostIp, self.hostPort))
        while True:
            cmd = input("JustHackIt->")
            _, addr = self.sock.recvfrom(8)
            # print(_, addr)
            self.sock.sendto(cmd.encode('utf-8'), addr)
            # print("send\n")
            recv, _ = self.sock.recvfrom(10240)
            print(recv.decode('gbk'))


if __name__ == "__main__":
    server = Server()
    server.main()
