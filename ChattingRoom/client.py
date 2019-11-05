"""
UDP Client
2019.10.28
"""

import socket
import threading
import tkinter as tk


class Client_wzk(object):

    def __init__(self, mytop):
        self.top = mytop
        self.ip_entry = tk.Entry(self.top, width=80, bd=4)
        self.port_entry = tk.Entry(self.top, width=80)
        self.send_entry = tk.Entry(self.top, width=80)
        self.recv_entry = tk.Entry(self.top, width=80)
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def startClient(self):
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # ip = input("Input your IP:\n")
        # portNum = int(input("Input your port number:\n"))
        ip = self.ip_entry.get()
        portNum = int(self.port_entry.get())
        print(ip, portNum)
        self.s.bind((ip, portNum))
        print('\033[0;32m Client \'{}, {}\' on\nYou can now start chatting...\033[0m\n'.format(ip, portNum))
        send_t = threading.Thread(target=self.send_thread, args=(self.s,))
        send_t.setDaemon(True)
        send_t.start()
        recv_t = threading.Thread(target=self.recv_thread, args=(self.s,))
        recv_t.setDaemon(True)
        recv_t.start()
        # send_t.join()    # if send_t ends, then recv has ended
        # s.close()    # close socket
        # return send_t

    # def close_socket(self, thread):
    #     thread.join()
    #     self.s.close()
    
    def send_thread(self, socket):
        # while True:
        # print("send thread")
        # inputData = bytes(input("->"), encoding='utf-8')    # waiting for input
        inputData = self.send_entry.get().encode('utf-8')
        # print("get send data")
        if inputData == b"exit":    # exit client
            # break
            return
        # indent = b' ' * 12    # 12 spaces
        socket.sendto(inputData, (self.hostIP, self.hostPort))

    def recv_thread(self, socket):
        while True:
        # print("recv thread")
            recvData, recvAddr = socket.recvfrom(1024)
            if recvAddr != (self.hostIP, self.hostPort):      # discard data not from host
                continue
            # print("get recv data")
            # print('\033[0;32m')
            # print(recvData.decode('utf-8'))
            # print('\033[0m')
            self.recv_entry.insert(0, recvData.decode('utf-8'))    # blocked

    def window(self):
        self.top.title('Chatting Room       by Echo Wang')
        tk.Label(self.top, text='Chatting Room       by Echo Wang')
        tk.Label(self.top, text='IP').grid(row=1)
        tk.Label(self.top, text='Port').grid(row=3)
        tk.Label(self.top, text='Send').grid(row=5)
        tk.Label(self.top, text='Recv').grid(row=7)
        self.ip_entry.grid(row=1, column=1)
        self.port_entry.grid(row=3, column=1)
        self.send_entry.grid(row=5, column=1)
        self.recv_entry.grid(row=7, column=1)
        startClient = tk.Button(self.top, text='Start Client', bg='green',
                                command=self.startClient)
        sendData = tk.Button(self.top, text='Send', bg='green',
                                command=lambda: self.send_thread(self.s))
        startClient.grid(row=3, column=2)
        sendData.grid(row=5, column=2)
        # self.top.mainloop()
        return 0


if __name__ == "__main__":
    top = tk.Tk()
    client = Client_wzk(top)
    client.window()
    top.mainloop()

