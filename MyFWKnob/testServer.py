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
        self.clientAddr = []
        self.passwds = ['123', 'abc']

    def tcpStart(self):
        """
        start tcp socket
        """
        self.s.bind((self.hostIP, self.hostPort))    # bind TCP socket
        self.s.listen(5)    # max clients to serve
        while True:
            sock, self.clientAddr = self.s.accept()
            t = threading.Thread(target=self.startAuth, args=(sock, ))
            t.setDaemon(True)
            t.start()

    def openPorts(self):
        """
        open port 21 for 15s using iptables
        """
        print("open ports")
        os.system("iptables -A INPUT -s {} -p 21 -j ACCEPT".format(self.clientAddr[0]))
        # os.system("ls")
        # wait 30s and clear authentication
        time.sleep(15)
        self.clearAuth()    # clear authentication after 15s

    def clearAuth(self):
        print("Clear authentication")
        os.system("iptables -D INPUT -s {} -p 21 -j ACCEPT".format(self.clientAddr[0]))

    def startAuth(self, sock):
        """
        autherize client ip if password is ok
        """
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
