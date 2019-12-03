"""
UDP Server
2019.10.28
"""


import socket
import time
from my_aes import PrpCrypt


class Server(object):

    def __init__(self):
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999
        self.pc = PrpCrypt("keyskeyskeyskeys")
        # 'ip,port':passwd
        self.passwds = {'127.0.0.1,9998': '9998', '127.0.0.1,9997': '9997', '127.0.0.1,9996': '9996'}

    def startServer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create socket object
        s.bind((self.hostIP, self.hostPort))
        chattingHistory = {}    # key for clientAddr, value for chatting data
        print("\033[0;32m Server on\033[0m\n")
        clients = []    # records for all clients
        while True:
            recvData, clientAddr = s.recvfrom(1024)    # recieve data
            decrypted_data = self.pc.decrypt(recvData)
            print("recv data", decrypted_data)
            if decrypted_data[0:6] == b"$login":    # login request
                info = decrypted_data[6:].split(b":")
                # client already registered
                try:
                    # passwd ok
                    if self.passwds[info[0].decode('utf-8')] == info[1].decode('utf-8'):
                        # s.sendto(b"pass", clientAddr)
                        s.sendto(self.pc.encrypt(b"pass"), clientAddr)
                    else:
                        # s.sendto(b"failed", clientAddr)
                        s.sendto(self.pc.encrypt(b"failed"), clientAddr)
                    print("continue")
                    continue
                # client not registered
                except KeyError:
                    # register
                    # self.register()
                    s.sendto(self.pc.encrypt(b"Please register first"), clientAddr)
                    self.passwds[info[0].decode('utf-8')] = info[1].decode('utf-8')    # register this account
            # elif decrypted_data[0:9] == b"$register":    # register request
            #     info = decrypted_data[9:].split(b":")
            chattingRcd = time.ctime() + '\n' + decrypted_data.decode('utf-8') + '\n'
            if clients.count(clientAddr) == 0:    # if this client is not recorded, then add it to list
                clients.append(clientAddr)
                chattingHistory[clientAddr] = chattingRcd     # add data to history
            else:
                chattingHistory[clientAddr] += chattingRcd
            showName = "Message From Client \'{0[0]}, {0[1]}\': \n".format(clientAddr)
            print('  ' + showName + decrypted_data.decode('utf-8'))    # server is listening
            if decrypted_data == b'cmd -h':    # search chatting history(what this client said)
                print("Client {} request to search chatting history\n".format(clientAddr))
                tips = "Chatting history of client {}\n".format(clientAddr).encode('utf-8')
                encrypted_his = self.pc.encrypt(tips + chattingHistory[clientAddr].encode('utf-8'))
                s.sendto(encrypted_his, clientAddr)
            # private chatting
            elif decrypted_data.split(b',', 3)[0] == b'cmd -prvt':    # msg format:[cmd],[dip],[dport],[msg],split by ','
                dip = decrypted_data.split(b',', 3)[1].decode('utf-8')
                dport = int(decrypted_data.split(b',', 3)[2].decode('utf-8'))
                msgBody = decrypted_data.split(b',', 3)[3]     # cut cmd info and leave msg body to send
                encrypted_send = self.pc.encrypt(showName.encode('utf-8') + msgBody + b'\n')    # encrypt
                s.sendto(encrypted_send, (dip, dport))
            # public chatting
            else:
                for addr in clients:    # forward data to all other clients
                    if addr != clientAddr:    # don't send to scr client
                        encrypted_send = self.pc.encrypt(showName.encode('utf-8') + decrypted_data + b'\n')
                        s.sendto(encrypted_send, addr)
        s.close()   # close socket


if __name__ == "__main__":
    server = Server()
    server.startServer()
