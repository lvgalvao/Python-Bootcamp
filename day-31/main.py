# from tkinter import *

# #-----CONST----#

# BACKGROUND_COLOR = "#B1DDC6"


# #-----FUNCTION----#

# #-----UI----#

# #-----WINDOW----#
# window = Tk()
# window.title("Flashy")
# window.config(padx=900, pady=626, background=BACKGROUND_COLOR)

# #-----CARDFRONT-----#
# canvas = Canvas(height=350, width=800)
# logo_img = PhotoImage(file="day-31/images/card_front.png")

# Label(window, image=logo_img).place(x = 60,y = 150)



# window.mainloop()

# !/usr/bin/python3
from tkinter import *
canvas = Canvas(height=350, width=800)
top = Tk()
L1 = PhotoImage(canvas, file="day-31/images/card_front.png")
L1.pack()
E1 = Entry(top, bd = 5)
E1.place(x = 60,y = 10)
L2 = Label(top,text = "Maths")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 5)
E2.place(x = 60,y = 50)

L3 = Label(top,text = "Total")
L3.place(x = 10,y = 150)
E3 = Entry(top,bd = 5)
E3.place(x = 60,y = 150)

B = Button(top, text = "Add")
B.place(x = 100, y = 100)
top.geometry("250x250+10+10")
top.mainloop()