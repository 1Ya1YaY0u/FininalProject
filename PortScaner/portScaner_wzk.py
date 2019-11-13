import socket
from concurrent.futures import ThreadPoolExecutor, wait
import tkinter as tk
from scapy.all import *


class PortScanner(object):
    def __init__(self, mytop):
        self.top = mytop
        self.ip_entry = tk.Entry(self.top, width=80)
        self.port_entry = tk.Entry(self.top, width=80)
        self.open_text = tk.Text(self.top, width=80)
        self.close_text = tk.Text(self.top, width=80)
        # self.sport = RandShort()
        self.sport = 9999
        # self.sip = '127.0.0.1'
        # print("randshort", self.sport)
        # self.dport = 8080
        # self.dip = '127.0.0.1'
        self.openDic = {}
        self.closeDic = {}

    def getTaskResult(self, task):
        # openPortList, closePortList = task.result()
        result = task.result()
        print(result)
        # self.openDic[ip] = ",".join(openPortList)
        # self.closeDic[ip] = ",".join(closePortList)
        # return result

    def scanOnePort(self, ip, port):
        openPortList = []
        closePortList = []
        try:
            # print(ip)
            # print(port)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            openPortList.append(str(port))
            result = "{}:{} open\n".format(ip, port)
            print(result)
            self.open_text.insert(0.0, result)
            s.close()
        except (ConnectionRefusedError):
            closePortList.append(str(port))
            result = "{}:{} closed\n".format(ip, port)
            print(result)
            self.close_text.insert(0.0, result)
        return openPortList, closePortList
        # self.openDic[ip] = ",".join(openPortList)
        # self.closeDic[ip] = ",".join(closePortList)

    def portScanner(self):
        # portList = list(map(int, portStr))
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ipStr = self.ip_entry.get().split(",")       # ip in ipstr, ipstr should be list
        getRes = self.port_entry.get().split(",")
        startPort = int(getRes[0])
        endPort = int(getRes[1])
        executor = ThreadPoolExecutor(9)
        print(startPort, endPort)
        allTasks = []
        for ip in ipStr:
            # openPortList = []
            # openPortList = []
            for port in range(startPort, endPort):
                # task = executor.submit(self.scanOnePort, ip, port)
                task = executor.submit(self.synScanOne, ip, port)
                allTasks.append(task)
                # openPortList, closePortList = task.result()
                # openPortList, closePortList = task.add_done_callback(self.getTaskResult)  #
                # task.add_done_callback(self.getTaskResult)    # 
                # try:
                #     # print(ip)
                #     # print(port)
                #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #     s.connect((ip, port))
                #     openPortList.append(str(port))
                #     print("{}:{} open".format(ip, port))
                #     s.close()
                # except (ConnectionRefusedError):
                #     closePortList.append(str(port))
                #     print("{}:{} closed".format(ip, port))
                # self.openDic[ip] = ",".join(openPortList)
                # self.closeDic[ip] = ",".join(closePortList)
        # wait(allTasks)
        # print(allTasks, allTasks.count())
        # self.open_text.insert(0.0, "Done")
        # self.close_text.insert(0.0, "Done")
        return self.openDic, self.closeDic

    def synScanOne(self, dip, dport):
        print("SYN scanner", dip, dport)
        syn = IP(dst=dip)/TCP(sport=self.sport, dport=dport, flags="S")
        resp = sr1(syn, timeout=2)
        if(resp.haslayer(TCP)):
            if(resp.getlayer(TCP).flags == 0x12):    # ack=1,syn=1
                rst = IP(dst=dip)/TCP(sport=self.sport, dport=dport, flags="R")
                sr(rst, timeout=2)    # send rst
                self.open_text.insert(0.0, "{}:{} open\n".format(dip, dport))
            elif(resp.getlayer(TCP).flags == 0x14):    # ack=1,rst=1
                self.close_text.insert(0.0, "{}:{} closed\n".format(dip, dport))

    def window(self):
        self.top.title('Port Scanner       by Echo Wang')
        tk.Label(self.top, text='Port Scanner       by Echo Wang')
        tk.Label(self.top, text='Dst IP').grid(row=1)
        tk.Label(self.top, text='Dst Port').grid(row=3)
        tk.Label(self.top, text='Open port').grid(row=5)
        tk.Label(self.top, text='Close port').grid(row=6)
        self.ip_entry.grid(row=1, column=1)
        self.port_entry.grid(row=3, column=1)
        self.open_text.grid(row=5, column=1)
        self.close_text.grid(row=6, column=1)
        startBtn = tk.Button(self.top, text='Start Scanner',
                             command=self.portScanner)
        # sendData = tk.Button(self.top, text='Send',
        #                         command=lambda: self.send_thread(self.s))
        startBtn.grid(row=3, column=2)
        # sendData.grid(row=5, column=2)
        # self.top.mainloop()
        return 0


if __name__ == "__main__":
    top = tk.Tk()
    myPortScanner = PortScanner(top)
    # odic, cdic = myPortScanner.portScanner(['127.0.0.1'], 8086, 8200)
    myPortScanner.window()
    top.mainloop()
    # print(odic, cdic)
