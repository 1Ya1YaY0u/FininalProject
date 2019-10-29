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
        print("Server on\n")
        print("***Alice***")
        while True:
            recvData, clientAddr = s.recvfrom(1024)    # recieve data
            # if recvData == b'exit':    # stop recieving data
                # time.sleep(0.1)
                # break
            chattingHistory.append(recvData)
            # print('Received data from client {}:{}\n'.format(clientAddr, recvData))
            print('\033[0;32m')    # Bob use red words
            print("            Bob:\n{}".format(recvData.decode('utf-8')))
            print('\033[0;31m')    # Alice use green words
            inputData = bytes(input("Alice:\n"), encoding='utf-8')    # waiting for input
            indent = b'            '    # 12 spaces
            s.sendto(indent + inputData, clientAddr)
        print('\033[0m')    # recover default colour
        s.close()   # close socket


if __name__ == "__main__":
    server = Server()
    server.startServer()
        
