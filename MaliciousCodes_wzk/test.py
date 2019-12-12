# import sys
# import os
# import runFlag
import subprocess


# # os.system(r'notepad C:\Users\zhikangwang\Desktop\test.txt')
# # a = sys.argv[1]
# # b = sys.argv[2]
# # print(a, b)
# try:
#     os.remove(r'C:\Users\zhikangwang\Desktop\test.txt')
# except WindowsError as e:
#     print(e)

# if runFlag.flag is False:
#     print("run")
#     # runFlag.flag = True
#     runFlag.setValue(True)
#     print(runFlag.flag)
# else:
#     print("stop")

# with open(r'./runflag.txt', 'r') as f:
#     content = f.read()
#     print(content)
# with open(r'./runflag.txt', 'w') as f:
#     if content == 'True':
#         print("true")
#     else:
#         print(content)
#         f.write("True")
# cmd = os.system('ipconfig')
# cmd = os.popen('md newfile')
# print(cmd.read())
# x = input()
# print(cmd.read())
subp = subprocess.Popen('ipconfig', shell=True, stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='gbk').communicate()
# p.wait()
# print(p.stdout.read())
# print(subp[0])
with open(r'C:\Users\zhikangwang\Desktop\a.txt', 'a') as f:
    f.write(subp[0])
# x = input()
