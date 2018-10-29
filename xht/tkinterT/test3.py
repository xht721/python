import tkinter as tk
window  = tk.Tk()
window.title("test3")
window.geometry("600x600")
var = tk.StringVar()
l = tk.Label(window,bg="yellow",width=10,textvariable=var)
l.pack()
def print_selection(v):
    var.set(v)
s = tk.Scale(window,label='try me',from_=1,to=10,orient=tk.HORIZONTAL,length=200,showvalue=True,
resolution=0.001,command=print_selection)
s.pack()
window.mainloop()