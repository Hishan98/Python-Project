import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import os

def startup(frame_search,frame_selection,frame_eb_error,root):
    frame_startup = tk.Frame(root, bg="white")
    frame_startup.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

    Label(frame_startup, text='Voice Commands:', font="Verdana 12 bold", padx=125, pady=5, bg="white").grid(row=0) 
    Label(frame_startup, text='Login', font="Verdana 8 bold", pady=5, bg="white").grid(row=1) 
    Label(frame_startup, text='Sign up', font="Verdana 8 bold", pady=5, bg="white").grid(row=2) 
    Label(frame_startup, text='Search', font="Verdana 8 bold", pady=5, bg="white").grid(row=3) 
    Label(frame_startup, text='Exit', font="Verdana 8 bold",  pady=5, bg="white").grid(row=4)

    frame_search.destroy()
    frame_selection.destroy()
    frame_eb_error.destroy()

def search_bar(frame_selection,frame_eb_error,frame_startup,root):
    frame_search = tk.Frame(root, bg="white")
    frame_search.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

    Label(frame_search, text='Voice Commands:', font="Verdana 12 bold", padx=125, pady=5, bg="white").grid(row=0) 
    Label(frame_search, text='First link', font="Verdana 8 bold",  pady=5, bg="white").grid(row=1)
    Label(frame_search, text='Second link', font="Verdana 8 bold",  pady=5, bg="white").grid(row=2)
    Label(frame_search, text='Thired link', font="Verdana 8 bold",  pady=5, bg="white").grid(row=3)
    Label(frame_search, text='Fourth link', font="Verdana 8 bold",  pady=5, bg="white").grid(row=4)
    Label(frame_search, text='Fifth link', font="Verdana 8 bold",  pady=5, bg="white").grid(row=5)
    Label(frame_search, text='Back', font="Verdana 8 bold",  pady=5, bg="white").grid(row=6)
    Label(frame_search, text='Delete', font="Verdana 8 bold",  pady=5, bg="white").grid(row=7)
    Label(frame_search, text='Backspace', font="Verdana 8 bold",  pady=5, bg="white").grid(row=8)
    Label(frame_search, text='Ok', font="Verdana 8 bold",  pady=5, bg="white").grid(row=9)
    Label(frame_search, text='Scroll up', font="Verdana 8 bold",  pady=5, bg="white").grid(row=10)
    Label(frame_search, text='Scroll Down', font="Verdana 8 bold",  pady=5, bg="white").grid(row=11)
    Label(frame_search, text='Exit', font="Verdana 8 bold",  pady=5, bg="white").grid(row=12)

    frame_startup.destroy()
    frame_selection.destroy()
    frame_eb_error.destroy()

def selection(frame_search,frame_eb_error,frame_startup,root):
    frame_selection = tk.Frame(root, bg="white")
    frame_selection.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)

    Label(frame_selection, text='Voice Commands:', font="Verdana 12 bold", padx=125, pady=5, bg="white").grid(row=0) 
    Label(frame_selection, text='Set', font="Verdana 8 bold",  pady=5, bg="white").grid(row=1)
    Label(frame_selection, text='Select', font="Verdana 8 bold",  pady=5, bg="white").grid(row=2)
    Label(frame_selection, text='Add to Cart', font="Verdana 8 bold",  pady=5, bg="white").grid(row=3)
    Label(frame_selection, text='Watch List', font="Verdana 8 bold",  pady=5, bg="white").grid(row=4)
    Label(frame_selection, text='Feedback', font="Verdana 8 bold",  pady=5, bg="white").grid(row=5)
    Label(frame_selection, text='Buy it Now', font="Verdana 8 bold",  pady=5, bg="white").grid(row=6)
    Label(frame_selection, text='Pay', font="Verdana 8 bold",  pady=5, bg="white").grid(row=7)
    Label(frame_selection, text='Back', font="Verdana 8 bold",  pady=5, bg="white").grid(row=8)
    Label(frame_selection, text='Exit', font="Verdana 8 bold",  pady=5, bg="white").grid(row=9)
    Label(frame_selection, text='First item', font="Verdana 8 bold",  pady=5, bg="white").grid(row=10)
    Label(frame_selection, text='Second item', font="Verdana 8 bold",  pady=5, bg="white").grid(row=11)
    Label(frame_selection, text='Thired item', font="Verdana 8 bold",  pady=5, bg="white").grid(row=8)
    Label(frame_selection, text='Fourth item', font="Verdana 8 bold",  pady=5, bg="white").grid(row=13)
    Label(frame_selection, text='Fifth item', font="Verdana 8 bold",  pady=5, bg="white").grid(row=14)

    frame_startup.destroy()
    frame_search.destroy()
    frame_eb_error.destroy()

def eb_error(frame_search,frame_selection,frame_startup,root):
    frame_eb_error = tk.Frame(root, bg="white")
    frame_eb_error.place(relwidth=0.8, relheight=0.7, relx=0.1, rely=0.03)
    
    Label(frame_eb_error, text='Voice Commands:', font="Verdana 12 bold", padx=125, pady=5, bg="white").grid(row=0) 
    Label(frame_eb_error, text='One step', font="Verdana 8 bold",  pady=5, bg="white").grid(row=1)
    Label(frame_eb_error, text='Two step', font="Verdana 8 bold",  pady=5, bg="white").grid(row=2)
    Label(frame_eb_error, text='Three step', font="Verdana 8 bold",  pady=5, bg="white").grid(row=3)
    Label(frame_eb_error, text='Four step', font="Verdana 8 bold",  pady=5, bg="white").grid(row=4)
    Label(frame_eb_error, text='Five step', font="Verdana 8 bold",  pady=5, bg="white").grid(row=5)
    Label(frame_eb_error, text='Back', font="Verdana 8 bold",  pady=5, bg="white").grid(row=6)
    Label(frame_eb_error, text='Ok', font="Verdana 8 bold",  pady=5, bg="white").grid(row=7)
    Label(frame_eb_error, text='Retry', font="Verdana 8 bold",  pady=5, bg="white").grid(row=8)
    Label(frame_eb_error, text='Exit', font="Verdana 8 bold",  pady=5, bg="white").grid(row=9)

    frame_startup.destroy()
    frame_search.destroy()
    frame_selection.destroy()