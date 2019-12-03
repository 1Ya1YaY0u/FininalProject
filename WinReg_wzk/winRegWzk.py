"""
Some functions need admin level permission
value of .docx was xxx.xxx.12
"""
import winreg
import tkinter as tk
import threading


class WinReg(object):
    def __init__(self, mytop):
        self.top = mytop
        self.key_entry = tk.Entry(self.top, width=100)
        self.valueName_entry = tk.Entry(self.top, width=100)
        self.value_entry = tk.Entry(self.top, width=100)
        self.result_text = tk.Text(self.top, width=100)
        self.hkeyRoot = winreg.HKEY_CLASSES_ROOT
        self.hkey = winreg.HKEY_LOCAL_MACHINE
        self.hkeyCuser = winreg.HKEY_CURRENT_USER
        self.bootPath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'    # HKEY_LOCAL_MACHINE
        self.bootApps = [('SecurityHealth', '%windir%\\system32\\SecurityHealthSystray.exe', 2), 
                         ('RTHDVCPL', '"C:\\Program Files\\Realtek\\Audio\\HDA\\RtkNGUI64.exe" -s', 1), 
                         ('RtHDVBg_PushButton', '"C:\\Program Files\\Realtek\\Audio\\HDA\\RAVBg64.exe" /IM', 1), 
                         ('QuickSet', 'c:\\Program Files\\Dell\\QuickSet\\QuickSet.exe', 1), 
                         ('ShadowPlay', '"C:\\Windows\\system32\\rundll32.exe" C:\\Windows\\system32\\nvspcap64.dll,ShadowPlayOnSystemStart', 1), 
                         ('TrueColor UI', 'C:\\Program Files\\TrueColor\\TrueColorUI.exe', 1), 
                         ('AdobeAAMUpdater-1.0', '"C:\\Program Files (x86)\\Common Files\\Adobe\\OOBE\\PDApp\\UWA\\UpdaterStartupUtility.exe"', 1), 
                         ('WavesSvc', '"C:\\Program Files\\Waves\\MaxxAudio\\WavesSvc64.exe" -Jack', 1), 
                         ('新值 #1', '', 1),
                         ('WindowsDefender', '"%ProgramFiles%\\Windows Defender\\MSASCuiL.exe"', 2),
                         ('test', 'value', 1)]
        self.txtPath = r'.txt\ShellNew'    # HKEY_CLASSES_ROOT\.txt\ShellNew
        self.txtBound = r'@%SystemRoot%\system32\notepad.exe,-470'
        # self.bmpPath = r'.bmp\ShellNew'
        # self.bmpBound = r'1@%systemroot%\system32\mspaint.exe,-59414'
        self.iePath = r'https\shell\open\command'    # HKEY_CLASSES_ROOT
        self.ieBound = r'"C:\Program Files\Internet Explorer\IEXPLORE.EXE" %1'
        self.ieHomePath = r'Software\Microsoft\Internet Explorer\Main'
        self.ieHomeUrl = 'https://www.bing.com/'

    def openKey(self, key, access=winreg.KEY_READ):
        return winreg.OpenKeyEx(self.hkey, key, access=access)

    def txtCheck(self):
        key = winreg.OpenKeyEx(self.hkeyRoot, self.txtPath, access=winreg.KEY_ALL_ACCESS)
        # key = self.openKey(self.txtPath)
        if winreg.QueryValueEx(key, 'ItemName')[0] == self.txtBound:
            # self.result_text.insert(100.100, "Txt ok\n")
            # print("txt ok")
            return True
        else:
            # print("no", winreg.QueryValueEx(key, 'ItemName')[0])
            self.result_text.insert(100.100, "Txt opened by:{}\n".format(winreg.QueryValueEx(key, 'ItemName')[0]))

    def ieCheck(self):
        key = winreg.OpenKeyEx(self.hkeyRoot, self.iePath, access=winreg.KEY_ALL_ACCESS)
        # key = self.openKey(self.txtPath)
        if winreg.QueryValueEx(key, '')[0] == self.ieBound:
            # self.result_text.insert(100.100, "IE ok:{}\n".format(self.ieBound))
            # print("IE ok")
            # self.ieHomeCheck()
            return self.ieHomeCheck()
        else:
            # print("no", winreg.QueryValueEx(key, 'ItemName')[0])
            self.result_text.insert(100.100, "IE is changed to:{}\n".format(winreg.QueryValueEx(key, '')[0]))
            self.ieHomeCheck()

    def ieHomeCheck(self):
        key = winreg.OpenKeyEx(self.hkeyCuser, self.ieHomePath, access=winreg.KEY_ALL_ACCESS)
        # key = self.openKey(self.txtPath)
        if winreg.QueryValueEx(key, 'Start Page')[0] == self.ieHomeUrl:
            # self.result_text.insert(100.100, "Homepage ok:{}\n".format(self.ieHomeUrl))
            # print("Homepage ok")
            return True
        else:
            # print("no", winreg.QueryValueEx(key, 'ItemName')[0])
            self.result_text.insert(100.100, "Homepage is changed to:{}\n".format(winreg.QueryValueEx(key, 'Start Page')[0]))

    def showBootApps(self):
        okey = winreg.OpenKeyEx(self.hkey, self.bootPath, 0, access=winreg.KEY_READ)
        i = 0
        bootApps = []
        while True:
            try:
                value = winreg.EnumValue(okey, i)
                bootApps.append(value)
                self.result_text.insert(100.100, "{}\n".format(value))
                i += 1
            except OSError:
                self.result_text.insert(100.100, "End\n")
                break
        # print(bootApps)
        return bootApps

    # def addReg(self, key, subKey):
    #     key = self.openKey(key)
    #     newReg = winreg.CreateKeyEx(key, subKey)
    #     return newReg

    # def deleteReg(self, key, subKey):
    #     key = self.openKey(key)
    #     try:
    #         winreg.DeleteKeyEx(key, subKey)
    #         return True
    #     except OSError as e:
    #         return e

    def addValue(self):
        key = self.key_entry.get()
        valueName = self.valueName_entry.get()
        value = self.value_entry.get()
        okey = self.openKey(key, access=winreg.KEY_ALL_ACCESS)    # open key
        try:
            winreg.SetValueEx(okey, valueName, 0, winreg.REG_SZ, value)
            self.result_text.insert(100.100, "Value Added\n")
        except OSError as e:
            self.result_text.insert(100.100, "{}\n".format(e))

    def deleteValue(self):
        key = self.key_entry.get()
        valueName = self.valueName_entry.get()
        okey = self.openKey(key, access=winreg.KEY_SET_VALUE)
        try:
            winreg.DeleteValue(okey, valueName)
            self.result_text.insert(100.100, "Value Deleted\n")
        except OSError as e:
            self.result_text.insert(100.100, "{}\n".format(e))

    def checkValue(self):
        key = self.key_entry.get()
        valueName = self.valueName_entry.get()
        okey = self.openKey(key)
        if valueName is None:    # no input
            i = 0
            while True:
                try:
                    value = winreg.EnumValue(okey, i)
                    self.result_text.insert(100.100, "{}\n".format(value))
                    i += 1
                except OSError:
                    self.result_text.insert(100.100, "End\n")
                    break
        else:
            try:
                value = winreg.QueryValueEx(okey, valueName)
                self.result_text.insert(100.100, "{}\n".format(value))
            except FileNotFoundError:
                self.result_text.insert(100.100, "Value name does not exist\n")

    def updateValue(self):
        key = self.key_entry.get()
        valueName = self.valueName_entry.get()
        value = self.value_entry.get()
        okey = self.openKey(key, access=winreg.KEY_SET_VALUE)
        try:
            winreg.SetValueEx(okey, valueName, 0, winreg.REG_SZ, value)
            self.result_text.insert(100.100, "Value Updated\n")
        except OSError as e:
            self.result_text.insert(100.100, "{}\n".format(e))

    def changeNotice(self):
        while True:
            # check boot apps
            hkeyMachine = winreg.OpenKeyEx(self.hkey, self.bootPath, 0, access=winreg.KEY_READ)
            i = 0
            bootApps = []
            while True:
                try:
                    value = winreg.EnumValue(hkeyMachine, i)
                    bootApps.append(value)
                    i += 1
                    # winreg.CloseKey(hkeyMachine)
                except OSError:
                    break
            # winreg.CloseKey(hkeyMachine)
            if bootApps != self.bootApps:
                self.result_text.insert(100.100, "Boot apps changed\n")
                break
            # check txt and IE
            elif self.txtCheck() is None or self.ieCheck() is None:
                # self.txtCheck()
                # self.ieCheck()
                break

    def window(self):
        t = threading.Thread(target=self.changeNotice)
        t.setDaemon(True)
        t.start()
        self.top.title('RegTool       by Echo Wang')
        tk.Label(self.top, text='RegTool       by Echo Wang')
        tk.Label(self.top, text='Key').grid(row=1)
        tk.Label(self.top, text='Value Name').grid(row=3)
        tk.Label(self.top, text='Value').grid(row=5)
        tk.Label(self.top, text='Result').grid(row=7)
        # tk.Label(self.top, text='Close port').grid(row=6)
        self.key_entry.grid(row=1, column=1, columnspan=7)
        self.valueName_entry.grid(row=3, column=1, columnspan=7)
        self.value_entry.grid(row=5, column=1, columnspan=7)
        self.result_text.grid(row=7, column=1, columnspan=7)
        addBtn = tk.Button(self.top, text='Add Value',
                           command=self.addValue)
        addBtn.grid(row=6, column=1)
        deleteBtn = tk.Button(self.top, text='Delete Value',
                              command=self.deleteValue)
        deleteBtn.grid(row=6, column=2)
        checkBtn = tk.Button(self.top, text='Check Value',
                             command=self.checkValue)
        checkBtn.grid(row=6, column=3)
        updateBtn = tk.Button(self.top, text='Update Value',
                              command=self.updateValue)
        updateBtn.grid(row=6, column=4)
        txtCheckBtn = tk.Button(self.top, text='Txt Check',
                                command=self.txtCheck)
        txtCheckBtn.grid(row=6, column=5)
        ieCheckBtn = tk.Button(self.top, text='IE Check',
                                command=self.ieCheck)
        ieCheckBtn.grid(row=6, column=6)
        bootAppsBtn = tk.Button(self.top, text='Show boot apps',
                                command=self.showBootApps)
        bootAppsBtn.grid(row=6, column=7)


if __name__ == "__main__":
    top = tk.Tk()
    myReg = WinReg(top)
    myReg.window()
    top.mainloop()
    # myReg.addValue(myReg.bootPath, 'test', 'value')
    # myReg.addValue('MyReg', 'test', 'value')
    # myReg.deleteValue(myReg.bootPath, 'test')
    # myReg.updateValue('MyReg', 'MyRegKey', 'hhh')
    # myReg.checkValue(myReg.bootPath)
    # print("000")
    # myReg.checkValue(myReg.bootPath, 'test')
    # myReg.txtCheck()
