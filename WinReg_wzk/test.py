import winreg


# key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'MyReg', access=winreg.KEY_ALL_ACCESS)
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'MyReg')
# winreg.DeleteValue(key, 'vn')
# print(key)
info = winreg.QueryInfoKey(key)
# print("info", info)
# qValue = winreg.QueryValue(winreg.HKEY_CURRENT_USER, 'MyReg')
# print('qvalue', qValue, type(qValue))
qValueEx = winreg.QueryValueEx(key, 'MyRegKey')
# winreg.SetValueEx(key, 'key1 value2', 0, winreg.REG_SZ, '1.2')
myRegKey2 = winreg.CreateKey(winreg.HKEY_CURRENT_USER, "MyRegKey2")
# key2 = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'MyRegKey2')
# print("open key2", key2)
# winreg.SetValue(winreg.HKEY_CURRENT_USER, 'MyReg', winreg.REG_SZ, 'setvalue')
# winreg.SetValueEx(key2, "key2 value2", 0, winreg.REG_SZ, "v22")
print('qvalueEx', qValueEx)

try:
    enumKey = winreg.EnumKey(key, 0)
    print('ekey', enumKey)
except OSError as e:
    print(e)
enmuValue = winreg.EnumValue(key, 0)
print('evalue', enmuValue)
# newKey = winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'NewKey')
# winreg.SetValueEx(newKey, 'newValue', 0, winreg.REG_SZ, "123")
# print("value of newkey", winreg.QueryValueEx(newKey, "newValue"))
# winreg.SetValueEx(newKey, 'newValue', 0, winreg.REG_SZ, "4456")    # update value
# print("value of newkey", winreg.QueryValueEx(newKey, "newValue"))
# winreg.DeleteValue(newKey, 'newvalue')
# infoNewKey = winreg.QueryInfoKey(newKey)
# print(infoNewKey)
# winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'NewKey')
