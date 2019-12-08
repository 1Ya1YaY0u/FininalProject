import sys
import os


# os.system(r'notepad C:\Users\zhikangwang\Desktop\test.txt')
# a = sys.argv[1]
# b = sys.argv[2]
# print(a, b)
try:
    os.remove(r'C:\Users\zhikangwang\Desktop\test.txt')
except WindowsError as e:
    print(e)