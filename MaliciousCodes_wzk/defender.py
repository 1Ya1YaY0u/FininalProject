import psutil
import os
import winreg


def runCheck():
    pids = psutil.pids()
    pname = []
    for pid in pids:
        ps = psutil.Process(pid)
        pname.append(ps.name())
    # if pname.count(psutil.Process().name()) > 2:
    while True:
        if "malware.exe" in pname:
            os.popen('taskkill /f /t /im malware.exe')
            # print(psutil.Process().name())
            # print(pname.count(psutil.Process().name()))
            # with open(self.flagPath, 'a') as f:
            #     f.write(pname.count(psutil.Process().name()))
            # print("0")
            return True
        # else:
            # f.wrte(1)
            # print(pname.count(psutil.Process().name()))
            # return True


def recoverReg():
    run = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'    # local machine
    txt = r'txtfile\shell\open\command'
    recoverTxt = r'%SystemRoot%\system32\NOTEPAD.EXE %1'
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, txt, access=winreg.KEY_ALL_ACCESS)
    try:
        # print(winreg.QueryValueEx(key, ""))
        winreg.SetValueEx(key, "", 0, winreg.REG_EXPAND_SZ, recoverTxt)
        # print("txt open changed\n")
    except WindowsError:
        # print(WindowsError)
        pass
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, run, access=winreg.KEY_ALL_ACCESS)
    try:
        # winreg.SetValueEx(key, "maliciousCode", 0, winreg.REG_SZ, self.scriptPath)    # add this script to Run key
        winreg.DeleteValue(key, "maliciousCode")
        # print("auto run\n")
    except WindowsError:
        # print(WindowsError)
        pass


if __name__ == "__main__":
    runCheck()
    recoverReg()