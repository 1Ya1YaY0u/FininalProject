import winreg
import tkinter as tk


class WinReg(object):
    def __init__(self, mytop):
        self.top = mytop
        self.key_entry = tk.Entry(self.top, width=100)
        self.valueName_entry = tk.Entry(self.top, width=100)
        self.value_entry = tk.Entry(self.top, width=100)
        self.result_text = tk.Text(self.top, width=100)
        self.hkeyRoot = winreg.HKEY_CLASSES_ROOT
        self.hkey = winreg.HKEY_LOCAL_MACHINE
        self.bootPath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'    # HKEY_LOCAL_MACHINE
        self.txtPath = r'.txt\ShellNew'    # HKEY_CLASSES_ROOT\.txt\ShellNew
        self.txtBound = r'@%SystemRoot%\system32\notepad.exe,-470'

    def openKey(self, key, access=winreg.KEY_READ):
        return winreg.OpenKeyEx(self.hkey, key, access=access)

    def txtCheck(self):
        key = winreg.OpenKeyEx(self.hkeyRoot, self.txtPath, access=winreg.KEY_ALL_ACCESS)
        # key = self.openKey(self.txtPath)
        if winreg.QueryValueEx(key, 'ItemName')[0] == self.txtBound:
            self.result_text.insert(100.100, "Txt opened by notepad.exe")
        else:
            # print("no", winreg.QueryValueEx(key, 'ItemName')[0])
            self.result_text.insert(100.100, "Txt open:{}".format(winreg.QueryValueEx(key, 'ItemName')[0]))

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
        if valueName == '':    # no input
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
            value = winreg.QueryValueEx(okey, valueName)
            self.result_text.insert(100.100, "{}\n".format(value))

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
    
    def window(self):
        self.top.title('RegTool       by Echo Wang')
        tk.Label(self.top, text='RegTool       by Echo Wang')
        tk.Label(self.top, text='Key').grid(row=1)
        tk.Label(self.top, text='Value Name').grid(row=3)
        tk.Label(self.top, text='Value').grid(row=5)
        tk.Label(self.top, text='Result').grid(row=7)
        # tk.Label(self.top, text='Close port').grid(row=6)
        self.key_entry.grid(row=1, column=1, columnspan=5)
        self.valueName_entry.grid(row=3, column=1, columnspan=5)
        self.value_entry.grid(row=5, column=1, columnspan=5)
        self.result_text.grid(row=7, column=1, columnspan=5)
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
