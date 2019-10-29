"""
UDP Client
2019.10.28
"""

import socket
import threading


class Client(object):

    def __init__(self):
        pass

    def startClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = input("Input IP:\n")
        portNum = int(input("Input port number:\n"))
        s.bind((ip, portNum))
        print('Client {} on\nYou can now start chatting...\n'.format(9998))
        print("***Bob***")
        while True:
            print('\033[0;32m')
            inputData = bytes(input("Bob:\n"), encoding='utf-8')    # waiting for input
            if inputData == b"exit":    # exit client
                break
            indent = b'            '    # 12 spaces
            s.sendto(indent + inputData, ('127.0.0.1', 9999))
            # print("Data sent\n")
            recvData, hostAddr = s.recvfrom(1024)
            # print("Received data from host {}:{}".format(hostAddr, recvData))
            print('\033[0;31m')
            print("            Alice:\n{}".format(recvData.decode('utf-8')))
        print('\033[0m')    # recover default colour
        s.close()    # close socket


if __name__ == "__main__":
    client = Client()
    client.startClient()

