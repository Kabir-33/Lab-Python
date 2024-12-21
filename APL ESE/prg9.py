# 9 program for designing a GUI using Tkinter

import tkinter as tk

root = tk.Tk()
root.title("My Tkinter GUI")
root.geometry("300x200")

def on_button_click():
    label.config(text="Button Clicked!")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

root.mainloop()
