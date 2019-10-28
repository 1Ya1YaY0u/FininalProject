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
        while True:
            print('Client {} on\nYou can now start chatting...\n'.format(9998))
            inputData = bytes(input("Input:\n"), encoding='utf-8')    # waiting for input
            if inputData == b"exit":    # exit client
                break
            s.sendto(inputData, ('127.0.0.1', 9999))
            print("Data sent\n")
            recvData, hostAddr = s.recvfrom(1024)
            print("Received data from host {}:{}".format(hostAddr, recvData))
        s.close()    # close socket


if __name__ == "__main__":
    client = Client()
    client.startClient()

