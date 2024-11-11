import tkinter as tk
master = tk.Tk()
master.geometry("200x200")

# Button 1 positioned near the top-right corner
b1 = tk.Button(master, text="Click me!")
b1.place(relx=0.9, rely=0.1, anchor="ne")

# Label placed explicitly near the top-left corner
l = tk.Label(master, text="I'm a Label")
l.place(relx=0.1, rely=0.1, anchor="nw")

# Button 2 centered in the window
b2 = tk.Button(master, text="GFG")
b2.place(relx=0.5, rely=0.5, anchor="center")

master.mainloop()