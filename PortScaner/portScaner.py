import socket
from concurrent.futures import ThreadPoolExecutor


class PortScanner(object):
    def __init__(self):
        # self.sport = RandShort()
        self.sport = 9999
        self.sip = '127.0.0.1'
        # print("randshort", self.sport)
        self.dport = 8080
        self.dip = '127.0.0.1'
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
            print("{}:{} open".format(ip, port))
            s.close()
        except (ConnectionRefusedError):
            closePortList.append(str(port))
            print("{}:{} closed".format(ip, port))
        return openPortList, closePortList
        # self.openDic[ip] = ",".join(openPortList)
        # self.closeDic[ip] = ",".join(closePortList)

    def portScanner(self, ipStr, startPort, endPort):
        # portList = list(map(int, portStr))
        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        executor = ThreadPoolExecutor(9)
        for ip in ipStr:
            # openPortList = []
            # openPortList = []
            for port in range(startPort, endPort):
                task = executor.submit(self.scanOnePort, ip, port)
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
        return self.openDic, self.closeDic


if __name__ == "__main__":
    myPortScanner = PortScanner()
    odic, cdic = myPortScanner.portScanner(['127.0.0.1'], 8086, 8200)
    # print(odic, cdic)
