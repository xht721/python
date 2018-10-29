import tkinter as tk 
import pickle
from tkinter import messagebox
window = tk.Tk()
window.title("tkinter test")
window.geometry("600x400")

def login():
    name = varname.get()
    passwd = varpass.get()
    try:
        with open("d:\\login.pickle ","rb") as f:
            loginInfo = pickle.load(f)
            if name in loginInfo:
                if loginInfo[name]==passwd:
                    print("exist")
                else:
                    print("not exist")
            else:
                tk.messagebox.showerror("error","error")
    except FileNotFoundError:
        with open("d:\\login.pickle","wb") as f:
            loginInfo = {"admin":"admin"}
            pickle.dump(loginInfo,f)


def sign():
    name = varname.get()
    print(name)
    passwd = varpass.get()
    print(passwd)
    with open("d:\\login.pickle","wb") as f:
        loginInfo={name:passwd}
        pickle.dump(loginInfo,f)

def do():
        print("do")
varname =tk.StringVar()
varpass =tk.StringVar()
varname.set("请输入用户名")

canvas = tk.Canvas(window,height=250,width=600)
image_file = tk.PhotoImage(file="d:\\welcome.png")
image = canvas.create_image(0,-20,anchor="nw",image = image_file)
canvas.pack()

name =  tk.Entry(window,textvariable=varname , )
password = tk.Entry(window,textvariable=varpass,show="*")
namelabel = tk.Label(window,text="用户名")
passlabel = tk.Label(window,text="密码")
name.place(x=200 ,y=250)
password.place(x=200 ,y=280)
namelabel.place(x=150 ,y=250)
passlabel.place(x=150 ,y=280)

btn_login = tk.Button(window,text="login ",command=login)
btn_sign_up = tk.Button(window,text="sign up ",command=sign)
btn_login.place(x=180 ,y=310)
btn_sign_up.place(x=280 ,y=310)


menubar = tk.Menu(window)

filemenu = tk.Menu(tearoff=0)
filemenu.add_command(label="new",command=do)
filemenu.add_command(label="save",command=do)
menubar.add_cascade(label="file",menu=filemenu)
window.config(menu=menubar)
window.mainloop()