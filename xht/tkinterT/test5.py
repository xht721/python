import tkinter as  tk
window = tk.Tk()
window.title("menu test")
window.geometry("600x400")
def do():
    pass
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label="new",command=do)
filemenu.add_command(label="save",command=do)
filemenu.add_separator()
filemenu.add_command(label="exit",command=window.quit)

editmenu = tk.Menu(menubar,tearoff=0)

menubar.add_cascade(label="file",menu=filemenu)
menubar.add_cascade(label="edit",menu=editmenu)

window.config(menu=menubar)
window.mainloop()