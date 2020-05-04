import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import os

root = tk.Tk()
root.title('GfG') 
apps =[]

myFont = tkFont.Font(family='Helvetica')

def addApp():
    # Firstbtn = tk.Button(root, text="First newei", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
    # Firstbtn.pack()
    frame1 = tk.Frame(root, bg="white")
    frame1.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)
    Label(frame1, text='First Name', font="Verdana 12 bold", padx=150, pady=5, bg="white").grid(row=0) 
    Label(frame1, text='First Name Name', font="Verdana 12 bold", pady=5, bg="white").grid(row=1) 
    Label(frame1, text='First Name Name Name', font="Verdana 12 bold", pady=5, bg="white").grid(row=2) 
    Label(frame1, text='First Name Name Name Name', font="Verdana 12 bold",  pady=5, bg="white").grid(row=3)
    frame.destroy()

def add2():
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)
    for i in range(20):
        Label(frame, text='First Name Name Name Name'+str(i), font="Verdana 12 bold",  pady=5, bg="white").grid(row=i)

    frame1.destroy()

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

w = Label(root, text='GeeksForGeeks.org!') 
w.pack() 

frame1 = tk.Frame(root, bg="white")
frame1.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.1)

# Buttons

Firstbtn = tk.Button(root, text="First Button", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
Firstbtn.pack()

Secondbtn = tk.Button(root, text="Second Button", padx=10, pady=5, fg="white", bg="#263D42", command=add2)
Secondbtn.pack()

# root.wait_visibility()
# addApp()
root.mainloop() 