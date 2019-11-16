from tkinter import *
 
 
# 插入函数（insert），在索隐处插入文字,
# 索引："insert"：在光标处插入
#       "end"：在Text对象的结尾插入
def insert_insert():
    # 获取entry输入的文字
    string = entry1.get()
    # 在光标处插入文字
    text1.insert("insert", string)
def insert_end():
    # 获取entry输入文字
    string = entry1.get()
    # 在text对象结尾插入文字
    text1.insert("end", string)
root = Tk()
root.minsize(200, 200)
# 在Entry组件中输入的字符都显示*（用于用户输入密码）
# entry1 = Entry(root, show="*")
# 创建entry对象，用于接受用户输入信息
entry1 = Entry(root)
entry1.pack()
button1 = Button(root, text="Button1_insert_insert", command=insert_insert)
button1.pack()
button2 = Button(root, text="Button2_insert_end", command=insert_end)
button2.pack()
text1 = Text(root)
text1.pack()
root.mainloop()