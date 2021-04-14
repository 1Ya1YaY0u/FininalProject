import os
import socket
import time
import threading

"""
firewall knob Server
"""


class Server(object):
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostIP = '127.0.0.1'
        self.hostPort = 62201
        self.passwds = ['123', 'abc']

    def tcpStart(self):
        self.s.bind((self.hostIP, self.hostPort))    # bind TCP socket
        self.s.listen(5)    # max clients to serve
        while True:
            sock, _ = self.s.accept()
            t = threading.Thread(target=self.startAuth, args=(sock, ))
            t.setDaemon(True)
            t.start()

    def openPorts(self):
        print("open ports")
        os.system("iptables -A INPUT -p 22 -j ACCEPT")
        # os.system("ls")
        # wait 30s and clear authentication
        time.sleep(5)
        self.clearAuth()

    def clearAuth(self):
        print("Clear authentication")
        os.system("iptables -D INPUT -p 22 -j ACCEPT")


    # start authentication
    def startAuth(self, sock):
        sock.send("Enter passwd to get access".encode('utf-8'))
        passwd = sock.recv(16).decode('utf-8')
        print("passwd", passwd)
        if passwd in self.passwds:
            print("passwd ok")
            sock.send("Accepted".encode('utf-8'))
            # open port 22/80
            print("ok sent")
            self.openPorts()
            # sock.close()
        else:
            print("passwd no")
            return


if __name__ == "__main__":
    server = Server()
    server.tcpStart()
