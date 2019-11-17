import winreg


class WinReg(object):
    def __init__(self):
        self.hkey = winreg.HKEY_CLASSES_ROOT
        self.bootPath = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        self.txtPath = r'.txt\ShellNew'    # HKEY_CLASSES_ROOT\.txt\ShellNew
        self.txtBound = r'@%SystemRoot%\system32\notepad.exe,-470'

    def openKey(self, key, access=winreg.KEY_READ):
        return winreg.OpenKeyEx(self.hkey, key, access=access)

    def txtCheck(self):
        key = self.openKey(self.txtPath)
        if winreg.QueryValueEx(key, 'ItemName')[0] == self.txtBound:
            print("ok")
        else:
            print("no", winreg.QueryValueEx(key, 'ItemName')[0])

    def addReg(self, key, subKey):
        key = self.openKey(key)
        newReg = winreg.CreateKeyEx(key, subKey)
        return newReg

    def deleteReg(self, key, subKey):
        key = self.openKey(key)
        try:
            winreg.DeleteKeyEx(key, subKey)
            return True
        except OSError as e:
            return e

    def addValue(self, key, valueName, value):
        key = self.openKey(key, access=winreg.KEY_ALL_ACCESS)
        try:
            winreg.SetValueEx(key, valueName, 0, winreg.REG_SZ, value)
            return True
        except OSError as e:
            print("in add:", e)
            return e

    def deleteValue(self, key, valueName):
        key = self.openKey(key, access=winreg.KEY_SET_VALUE)
        try:
            winreg.DeleteValue(key, valueName)
            return True
        except OSError as e:
            print("delete:", e)
            return e

    def checkValue(self, key, valueName=None):
        key = self.openKey(key)
        if valueName is None:
            i = 0
            while True:
                try:
                    value = winreg.EnumValue(key, i)
                    print("enum value", value)
                    i += 1
                except OSError:
                    return
        else:
            value = winreg.QueryValueEx(key, valueName)
            print("query value", value)

    def updateValue(self, key, valueName, value):
        key = self.openKey(key, access=winreg.KEY_SET_VALUE)
        try:
            winreg.SetValueEx(key, valueName, 0, winreg.REG_SZ, value)
            print("updated")
        except OSError as e:
            print("in update:", e)
            return e


if __name__ == "__main__":
    myReg = WinReg()
    # myReg.addValue(myReg.bootPath, 'test', 'value')
    # myReg.addValue('MyReg', 'test', 'value')
    # myReg.deleteValue(myReg.bootPath, 'test')
    # myReg.updateValue('MyReg', 'MyRegKey', 'hhh')
    # myReg.checkValue(myReg.bootPath)
    # print("000")
    # myReg.checkValue(myReg.bootPath, 'test')
    myReg.txtCheck()
