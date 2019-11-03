"""
UDP Server
2019.10.28
"""


import socket


class Server(object):

    def __init__(self):
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999

    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create socket object
        s.bind((self.hostIP, self.hostPort))
        chattingHistory = {}    # key for clientIP, value for chatting data
        print("\033[0;32m Server on\033[0m\n")
        clients = []    # records for all clients
        while True:
            recvData, clientAddr = s.recvfrom(1024)    # recieve data
            if clients.count(clientAddr) == 0:    # if this client is not recorded, then add it to list
                clients.append(clientAddr)
            # if recvData == sys.stdin(exit):    # stop recieving data
            chattingHistory[clientAddr[0]] = recvData
            showName = "Message From Client \'{0[0]}, {0[1]}\': \n".format(clientAddr)
            print('  ' + showName + recvData.decode('utf-8'))      # server is listening
            for addr in clients:    # forward data to all other clients
                if addr != clientAddr:
                    s.sendto(showName.encode('utf-8') + recvData, addr)
        s.close()   # close socket


if __name__ == "__main__":
    server = Server()
    server.startServer()
        
