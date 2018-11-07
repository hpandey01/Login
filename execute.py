# decoded_data = base64.b64decode(name.decode())
# 		f1.write(str(decoded_data)[2:-1])                   C:\LOGIN\setup\dist\setup
from tkinter import *
import base64
import os
import sys
import subprocess
from threading import Thread

root=Tk()
root.title("Authentication")
frame=Frame(root,width=600, height=400)
frame.pack()

display=StringVar()

def process(name, password):
	os.chdir("C:\\LOGIN\\login\\dist\\login")
	os.system('"login.exe '+name+' '+password+'"')
	sys.exit()

def decrypt(text):
    code=''
    for i in range(1,(len(text)//7)+1):
        code+=text[7*i-1]
    return code

def execute():
	code=tbox1.get()
	f1=open("C:\\LOGIN\\setup\\dist\\setup\\setup.txt","r")
	arr=f1.readlines()
	name=decrypt(arr[0][:-1])
	password=decrypt(arr[1][:-1])
	code1=decrypt(arr[2])
	f1.close()
	if int(code)==int(code1):
		Thread(target=process, args=(name, password,)).start()
	else:
		display.set("Incorrect Password")
	return


title=Label(text="AUTHENTICATION")
title.config(font="Arial 18 bold", foreground="black")
title.place(x=29.7, y=50, height=28.6, width=584)

link = Label(text="Password: ")
link.config(font="Arial 12 bold", foreground="black")
link.place(x=123.6, y=128.3, height=33.2, width=127.3)

tbox1 = Entry(frame)
tbox1.config(font="Arial 12")
tbox1.place(x=290, y=128.3, height=28.2, width=200)

button1 = Button(frame, text="LOGIN", command=execute)
button1.config(font="Arial 14 bold", foreground="white", background="#fa0604")
button1.place(x=220.7, y=200, height=29.9, width=164.1)

info=Label(text="designed an developed by Himanshu Pandey")
info.config(font="Arial 10 bold", foreground="black")
info.place(x=-30, y=350, height=28.6, width=484)

status=Label(textvariable=display)
status.config(font="Arial 18 italic", foreground="black")
status.place(x=20.7, y=260, height=28.6, width=584)

root.mainloop()