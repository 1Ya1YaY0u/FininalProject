"""
UDP Client
2019.10.28
"""
import socket
import threading
class Client(object):
    def __init__(self):
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999
    def startClient(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ip = input("Input your IP:\n")
        portNum = int(input("Input your port number:\n"))
        s.bind((ip, portNum))
        print('\033[0;32m Client \'{}, {}\' on\nYou can now start chatting...\033[0m\n'.format(ip, portNum))
        send_t = threading.Thread(target=self.send_thread, args=(s,))
        send_t.start()
        recv_t = threading.Thread(target=self.recv_thread, args=(s,))
        recv_t.start()
        send_t.join()    # if send_t ends, then recv has ended
        s.close()    # close socket
    def send_thread(self, socket):
        while True:
            inputData = bytes(input("->"), encoding='utf-8')    # waiting for input
            if inputData == b"exit":    # exit client
                break
            # indent = b' ' * 12    # 12 spaces
            socket.sendto(inputData, (self.hostIP, self.hostPort))
    def recv_thread(self, socket):
        while True:
            recvData, recvAddr = socket.recvfrom(1024)
            if recvAddr != (self.hostIP, self.hostPort):      # discard data not from host
                break
                continue
            print('\033[0;32m')
            print(recvData.decode('utf-8'))
            print('\033[0m')
if __name__ == "__main__":
    client = Client()
    client.startClient()