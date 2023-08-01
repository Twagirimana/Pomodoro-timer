import math
from tkinter import *

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FFFFFF"
FONT_NAME = "courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
time = None


def reset_timer():
    window.after_cancel("time")
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    sign.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        signs = ""
        work_sessions = math.floor(reps / 2)
        for n in range(work_sessions):
            signs += "✔"
        sign.config(text=signs)


window = Tk()
window.title("Pomodoro")
window.minsize(width=500, height=400)
window.config(padx=100, pady=50, bg=YELLOW)
# count_down(5)

timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)

start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

sign = Label(bg=YELLOW, fg=GREEN)
sign.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00=00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


window.mainloop()
