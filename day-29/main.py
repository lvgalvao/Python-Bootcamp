from curses import window
from email.mime import image
from tkinter import *
from tkinter import ttk
root = Tk() ### Creates an instance of the Tk class, 
            ### which initializes Tk and creates its associated Tcl interpreter. It also creates a toplevel window,
            ### known as the root window, which serves as the main window of the application.

root.title("Password Manager")
root.config(padx=20, pady=20)

canvas = Canvas(height=200 , width= 200)
logo_img = PhotoImage(file="day-29/src/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()
root.mainloop() ### Mantein the application 
just it

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

upupupudododi