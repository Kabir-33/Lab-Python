import tkinter as tk
root=tk.Tk()
root.title("Pack Example")
button1=tk.Button(root,text="Button 1")
button2=tk.Button(root,text="Button 2")
button3=tk.Button(root,text="Button 3")

button1.grid()
button2.grid()
button3.grid()

root.mainloop()