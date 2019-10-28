"""
UDP Server
2019.10.28
"""

import socket
import threading
import time


class Server(object):

    def __init__(self):
        pass

    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create socket object
        s.bind(('127.0.0.1', 9999))
        chattingHistory = []
        while True:
            print("Server on\n")
            recvData, clientAddr = s.recvfrom(1024)    # recieve data
            if recvData == b'exit':    # stop recieving data
                # time.sleep(0.1)
                break
            chattingHistory.append(recvData)
            print('Received data from client {}:{}\n'.format(clientAddr, recvData))
            s.sendto(b'Data recieved', clientAddr)
        s.close()   # close socket


if __name__ == "__main__":
    server = Server()
    server.startServer()
        
