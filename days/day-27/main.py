from tkinter import *

RATIO_MILES_TO_KM = 1.609

def convert_to_km():
    miles = float(miles_input.get())
    new_text = miles * 1.609
    result_label.config(text=f"{new_text}")

root = Tk()
root.title("Mile to Km Converter")
root.config(padx=20, pady=20)

# create the labels
# is equal to
is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=1, row=2)
# {result}
result_label = Label(text="0")
result_label.grid(column=2, row=2)
# Km
km_label = Label(text="Km")
km_label.grid(column=3, row=2)
# Miles
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)
# create the button
button_convert = Button(text="Calculate", command=convert_to_km)
button_convert.grid(column=2, row=3)
# create the input box
miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)
# create the exit button
button_exit = Button(text="Quit", command=root.destroy)
button_exit.grid(column=3, row=4)

root.mainloop()