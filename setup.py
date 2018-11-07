from tkinter import *
import string
import random

root=Tk()
root.title("Setup Wizard")
frame=Frame(root, width=600, height=540)
frame.pack()
display=StringVar()

def encrypt_text(text):
    code=''
    for i in range(1,(7*(len(text)))+1):
    	if i%7==0:
    		code+=text[i//7-1]
    	else:
    		if (i%2==0):
    			code+=random.choice(string.ascii_letters)
    		else:
    			code+=random.choice('0123456789')
    return code

def encrypt_code(text):
	code=''
	for i in range(1,(7*(len(text)))+1):
		if i%7==0:
			code+=text[i//7-1]
		else:
			code+=random.choice('0123456789')
	return code

def setup():
	name=tbox1.get()
	password=tbox2.get()
	code=tbox3.get()
	name = encrypt_text(name)
	password = encrypt_text(password)
	code = encrypt_code(code)
	if (tbox1.get()!="" and tbox2.get()!=""):
		f1=open("setup.txt","w")
		f1.write(name+"\n"+password+"\n"+code)
		f1.close()
		display.set("Changes Saved..")
	else:
		if tbox1.get()=="":
			display.set("Empty Username")
		else:
			display.set("Empty Password")


title=Label(text="WELCOME SETUP WIZARD")
title.config(font="Arial 18 bold", foreground="black")
title.place(x=29.7, y=50, height=28.6, width=584)

link = Label(text="Username: ")
link.config(font="Arial 12 bold", foreground="black")
link.place(x=123.6, y=128.3, height=33.2, width=127.3)

tbox1 = Entry(frame)
tbox1.config(font="Arial 12")
tbox1.place(x=290, y=128.3, height=28.2, width=200)

name = Label(text="Password: ")
name.config(font="Arial 12 bold", foreground="black")
name.place(x=93.6, y=188.3,height=33.2,width=187.3)

tbox2 = Entry(frame)
tbox2.config(font="Arial 12")
tbox2.place(x=290, y=188.3, height=28.2, width=200)

code = Label(text="Numerical Password: ")
code.config(font="Arial 12 bold", foreground="black")
code.place(x=93.6, y=248.3,height=33.2,width=187.3)

tbox3 = Entry(frame)
tbox3.config(font="Arial 12")
tbox3.place(x=290, y=248.3, height=28.2, width=200)

button1 = Button(frame, text="SAVE", command=setup)
button1.config(font="Arial 14 bold", foreground="white", background="#fa0604")
button1.place(x=220.7, y=340, height=29.9, width=164.1)

info=Label(text="designed an developed by Himanshu Pandey")
info.config(font="Arial 10 bold", foreground="black")
info.place(x=-30, y=500, height=28.6, width=484)

status=Label(textvariable=display)
status.config(font="Arial 18 italic", foreground="black")
status.place(x=20.7, y=400, height=28.6, width=584)

root.mainloop()