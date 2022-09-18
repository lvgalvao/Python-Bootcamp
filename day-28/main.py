from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
FILE = "day-28/src/tomato.png"
reps = 1
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button():
    global marks
    root.after_cancel(timer)
    label_timer.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_timer.config(text="")
    return

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
    global reps

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Long break", fg=RED)
    
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        global timer
        timer = root.after(1000, count_down, count - 1)
    elif count== 0:
        global marks
        reps += 1
        start_time()
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_timer.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Pomodoro")
root.config(padx=100, pady=50, bg=YELLOW)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label_timer.grid(column=2, row=1)

tomato_img = PhotoImage(file=FILE)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

check_timer = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
check_timer.grid(column=2, row=4)

# start button
button_start = Button(text="Start", highlightthickness=0,  bg=YELLOW, command=start_time)
button_start.grid(column=1, row=3)

# reset button
button_reset = Button(text="Reset", highlightthickness=0, bg=YELLOW, command=reset_button)
button_reset.grid(column=3, row=3)


root.mainloop()