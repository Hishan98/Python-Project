import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import os

root = tk.Tk()
root.title('Talk & Shop') 
apps =[]

myFont = tkFont.Font(family='Helvetica')

canvas = tk.Canvas(root, height=500, width=500, bg="#263D42")
canvas.pack()

w = Label(root, text='Team Squadra Production') 
w.pack() 

frame_search = tk.Frame(root, bg="white")
frame_search.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

frame_selection = tk.Frame(root, bg="white")
frame_selection.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

frame_eb_error = tk.Frame(root, bg="white")
frame_eb_error.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

frame_startup = tk.Frame(root, bg="white")
frame_startup.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

# Buttons

#  import ebaygui_changes as ebaygui_changes

def serchBar():
    from View_ebaygui_changes import search_bar as ebaygui_search_bar
    ebaygui_search_bar(frame_selection,frame_eb_error,frame_startup,root)

def selectionBar():
    from View_ebaygui_changes import selection as ebaygui_selection
    ebaygui_selection(frame_search,frame_eb_error,frame_startup,root)

def ebError():
    from View_ebaygui_changes import eb_error as ebaygui_eb_error
    ebaygui_eb_error(frame_search,frame_selection,frame_startup,root)

def StrtuP():
    from View_ebaygui_changes import startup as ebaygui_startup
    ebaygui_startup(frame_search,frame_selection,frame_eb_error,root)

btn_search = tk.Button(root, text="Search", padx=10, pady=5, fg="white", bg="#263D42", 
command=serchBar)
btn_search.pack()

btn_selection = tk.Button(root, text="Selection", padx=10, pady=5, fg="white", bg="#263D42", 
command=selectionBar)
btn_selection.pack()

btn_eb_error = tk.Button(root, text="eBay error", padx=10, pady=5, fg="white", bg="#263D42", 
command=ebError)
btn_eb_error.pack()

btn_startup = tk.Button(root, text="Startup", padx=10, pady=5, fg="white", bg="#263D42", 
command=StrtuP)
btn_startup.pack()

root.wait_visibility()
StrtuP()
import Main as mainPrograme
mainPrograme.site_selection()
root.mainloop() 