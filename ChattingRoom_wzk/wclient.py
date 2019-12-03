"""
UDP Client
2019.10.28
"""

import socket
import threading
import tkinter as tk
from my_aes import PrpCrypt


class Client_wzk(object):

    def __init__(self, mytop):
        self.top = mytop
        self.ip_entry = tk.Entry(self.top, width=80)
        self.port_entry = tk.Entry(self.top, width=80)
        self.passwd_entry = tk.Entry(self.top, width=80)
        self.send_entry = tk.Entry(self.top, width=80)
        self.recv_entry = tk.Text(self.top, width=80)
        self.hostIP = '127.0.0.1'
        self.hostPort = 9999
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.pc = PrpCrypt("keyskeyskeyskeys")

    def startClient(self, ip, portNum):
        # ip = self.ip_entry.get()
        # portNum = int(self.port_entry.get())
        # passwd = self.passwd_entry.get()
        print("start client", ip, portNum)
        # self.s.bind((ip, portNum))
        # print(self.s)
        print('\033[0;32m Client \'{}, {}\' on\nYou can now start chatting...\033[0m\n'.format(ip, portNum))
        send_t = threading.Thread(target=self.send_thread, args=(self.s,))      # send thread
        send_t.setDaemon(True)
        send_t.start()
        recv_t = threading.Thread(target=self.recv_thread, args=(self.s,))      # recv thread
        recv_t.setDaemon(True)
        recv_t.start()
    
    def register(self):
        ip = self.ip_entry.get()
        portNum = int(self.port_entry.get())
        passwd = self.passwd_entry.get()
        # print(ip, portNum, passwd)
        self.recv_entry.insert(0.0, "Registered:{}\n{}\n{}\n".format(ip, portNum, passwd))

    def login(self):
        ip = self.ip_entry.get()
        portNum = self.port_entry.get()
        self.s.bind((ip, int(portNum)))
        # for i in range(5):    # 5 times to input correct passwd
        # portNum = int(self.port_entry.get())
        passwd = self.passwd_entry.get()
        loginInfo = '$login' + ip + "," + portNum + ":" + passwd
        encrypt_data = self.pc.encrypt(loginInfo.encode('utf-8'))
        self.s.sendto(encrypt_data, (self.hostIP, self.hostPort))
        print(loginInfo)
        resp, _ = self.s.recvfrom(1024)    # response from server
        if self.pc.decrypt(resp) == b"Please register first":
            self.recv_entry.insert(0.0, "Account not exisit, register first\n")
        elif self.pc.decrypt(resp) == b"pass":    # account and passwd ok, then start client
            self.recv_entry.insert(0.0, "Login\n")
            print("params", ip, portNum)
            self.startClient(ip, int(portNum))
        elif self.pc.decrypt(resp) == b"failed":    # varifi failed, can try again, but not more than 5 times
            # self.ip_entry.delete(0,20)
            # self.port_entry.delete(0,20)
            self.passwd_entry.delete(0, 20)
            self.s.close()    # need to improve
            self.recv_entry.insert(0.0, "Wrong passwd for this account")
            print("try again")
        else:    # unexpected resp
            self.passwd_entry.delete(0, 20)
            self.s.close()
            self.recv_entry.insert(0.0, "Wrong passwd for this account")
            print("error")
            # break

    def send_thread(self, socket):
        print("send thread")
        inputData = self.send_entry.get().encode('utf-8')
        self.send_entry.delete(0, 100)
        if inputData == b"exit":    # exit client
            # break
            return
        encrypt_data = self.pc.encrypt(inputData)
        socket.sendto(encrypt_data, (self.hostIP, self.hostPort))

    def recv_thread(self, socket):
        while True:
            recvData, recvAddr = socket.recvfrom(1024)
            print("***recvdata", recvData)
            decrypted_data = self.pc.decrypt(recvData)
            print("***decdata", decrypted_data)
            if recvAddr != (self.hostIP, self.hostPort):      # discard data not from host
                continue
            self.recv_entry.insert(100.100, decrypted_data.decode('utf-8'))    # blocked

    def window(self):
        self.top.title('Chatting Room       by Echo Wang')
        tk.Label(self.top, text='Chatting Room       by Echo Wang')
        tk.Label(self.top, text='IP').grid(row=1)
        tk.Label(self.top, text='Port').grid(row=3)
        tk.Label(self.top, text='Passwd').grid(row=5)
        tk.Label(self.top, text='Send').grid(row=7)
        tk.Label(self.top, text='Recv').grid(row=9)
        self.ip_entry.grid(row=1, column=1)
        self.port_entry.grid(row=3, column=1)
        self.passwd_entry.grid(row=5, column=1)
        self.send_entry.grid(row=7, column=1)
        self.recv_entry.grid(row=9, column=1)
        login = tk.Button(self.top, text='Login', bg='green',
                          command=self.login)
        sendData = tk.Button(self.top, text='Send', bg='green',
                             command=lambda: self.send_thread(self.s))
        register = tk.Button(self.top, text='Register', bg='green',
                          command=self.register)
        register.grid(row=3, column=2)
        login.grid(row=5, column=2)
        sendData.grid(row=7, column=2)
        return 0


if __name__ == "__main__":
    top = tk.Tk()
    # top.geometry('800x500')
    client = Client_wzk(top)
    client.window()
    top.mainloop()
# login btn not ended, maybe thread things
