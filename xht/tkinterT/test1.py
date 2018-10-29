import tkinter as tk
window  = tk.Tk()
window.title("my window")
window.geometry('200x100')
var = tk.StringVar()
l=tk.Label(window,textvariable=var,bg="blue",width=12,height=2)
l.pack()
on_flag = False
def hit():
    global on_flag
    if on_flag == True:
        var.set("you hit me")
        on_flag = False
    else:
        var.set("")
        on_flag = True
b = tk.Button(window,text="hit",width=10,height=1,command=hit)
b.pack()

window.mainloop()