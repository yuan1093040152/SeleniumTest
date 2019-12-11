#coding=utf-8
from tkinter import *
from tkinter import messagebox


#第一个函数：用于关闭窗口提示
def close_window():
	messagebox.showinfo(title="警告",message="重新选一个")

	return

#第二个函数：定义“喜欢”提示
def Love():
	love = Toplevel(window)
	love.geometry("300x100+250+250")
	love.title("我也喜欢你！")
	label = Label(love,text = "我也喜欢你呀！",font = ("微软雅黑",20))
	label.pack()
	btn = Button(love,text = "在一起吧",width = 10,height = 2,command = close_all_window)
	btn.pack()
	love.protocol("WM_DELETE_WINDOW",close_love)

def close_love():
	return
#关闭所有窗口

def close_all_window():
	window.destroy()

#定义不喜欢按钮
def no_Love():
	no_lone = Toplevel(window)
	no_lone.geometry("300x100+520+260")
	no_lone.title("重新选")
	label = Label(no_lone, text="回去重新选（坏笑）！", font=("微软雅黑", 20))
	label.pack()
	btn = Button(no_lone, text="好", width=10, height=2, command=no_lone.destroy)
	btn.pack()
	no_lone.protocol("WM_DELETE_WINDOW", close_no_love)

def close_no_love():
	no_Love()
#创建窗口
window = Tk()
#窗口标题
window.title("嗨，小姐姐")
#窗口大小
window.geometry("450x420+500+240")
btn = Button(text = "确定")
window.protocol("WM_DELETE_WINDOW", close_window)
#标签控件
label = Label(window,text = "观察你很久了",font = ("微软雅黑",15),fg = "red")
label.grid(row = 0, column = 0)

label = Label(window,text = "做我女朋友体好不好？",font = ("微软雅黑",20))
label.grid(row = 1, column = 1,sticky = E)

#插入图片
#插入的图片可以自行修改，但图片像素不要太大（大概300x300左右就行了）
photo = PhotoImage(file = "./520.png")
image_Lable = Label(window,image = photo)
image_Lable.grid(row = 2,columnspan = 2)
#喜欢按钮插件
btn = Button(window, text="好", width=15, height=2, command=Love)
btn.grid(row = 3,column = 0,sticky = W)
#不喜欢按钮插件
btn = Button(window, text="不好", command=no_Love)
btn.grid(row = 3,column = 1,sticky = E)

#显示窗口，消息循坏
window.mainloop()




# 最后使用pyinstaller打包程序为exe文件后就可以发送给她啦！！具体操作如下：

# 在保存.py文件的目录下，运行cmd，没有pyinstaller的先pip安装，已经有了的直接pyinstaller –F –w xxx.py即可。