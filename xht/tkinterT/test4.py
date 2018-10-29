import tkinter as tk  
window=tk.Tk()
window.title("canvas test")
window.geometry("600x400")

def move():
    pass
canvas = tk.Canvas(window,bg="yellow",height=500,width=500)
image_file=tk.PhotoImage(file="d:\\a.png")
image = canvas.create_image(10,10,anchor="e",image=image_file)
b = tk.Button(window,text="move",command=move)
b.pack()

canvas.pack()
window.mainloop()