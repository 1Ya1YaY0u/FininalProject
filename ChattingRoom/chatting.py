"""
Chatting room
2019.10.27
"""

# import 

# buffer = [b'1', b'2', b'3']
# print(buffer)
# print(type(buffer[0]))
# b = b''.join(buffer)
# print(b)
# print(type(b))

# sen = "you \nme"
# print('*')
# print(sen)
# sen = "you \rme"
# print('*')
# print(sen)
# sen = "you \r\nme"
# print('*')
# print(sen)

# addr = (1, 'a')
# print("content {0[0]} {0[1]}".format(addr))

# a = input("lala")
# a = "lala"
# # print(type(a))
# print('\033[0;31m')
# print(a)


# import sys
# print(sys.path)
# import asyncio


# @asyncio.coroutine
# def io():
#     a = input("input")
#     print(a)

# @asyncio.coroutine
# def hello():
#     print("Hello world!")
#     # 异步调用asyncio.sleep(1):
#     r = yield from io()
#     print("Hello again!")

# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# # loop.run_until_complete(hello())
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
print("\033[0;32m Client \'{}, {}\' \033[0m")

