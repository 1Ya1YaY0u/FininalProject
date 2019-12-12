# import sys
import os
# import runFlag


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
cmd = os.popen('ipconfig')
print(cmd.read())
