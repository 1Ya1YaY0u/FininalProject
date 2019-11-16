"""
UDP Server
2019.10.28
"""


import socket
import time


class Server(object):
    def __init__(self):
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999
    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create socket object
        s.bind((self.hostIP, self.hostPort))
        chattingHistory = {}    # key for clientIP, value for chatting data
        chattingHistory = {}    # key for clientAddr, value for chatting data
        print("\033[0;32m Server on\033[0m\n")
        clients = []    # records for all clients
        while True:
            recvData, clientAddr = s.recvfrom(1024)    # recieve data
            chattingRcd = time.ctime() + '\n' + recvData.decode('utf-8') + '\n'
            if clients.count(clientAddr) == 0:    # if this client is not recorded, then add it to list
                clients.append(clientAddr)
                chattingHistory[clientAddr] = chattingRcd     # add data to history
            else:
                chattingHistory[clientAddr] += chattingRcd
            # if recvData == sys.stdin(exit):    # stop recieving data
            chattingHistory[clientAddr[0]] = recvData
            if recvData == b'cmd -h':    # search chatting history(what this client said)
                print("Client {} request to search chatting history\n".format(clientAddr))
                tips = "\033[0;33mChatting history of client {}\033[0m\n".format(clientAddr).encode('utf-8')
                s.sendto(tips + chattingHistory[clientAddr].encode('utf-8'), clientAddr)
                continue

            showName = "Message From Client \'{0[0]}, {0[1]}\': \n".format(clientAddr)
            print('  ' + showName + recvData.decode('utf-8'))      # server is listening
            for addr in clients:    # forward data to all other clients
                if addr != clientAddr:
                    s.sendto(showName.encode('utf-8') + recvData, addr)
        s.close()   # close socket
if __name__ == "__main__":
    server = Server()
    server.startServer()