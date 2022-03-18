from cgitb import text
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_Button_Pressed():
    window.after_cancel(timer)
    canvas.itemconfig(timer_Text, text = "00:00")
    timer_Label.config(text = "Timer")
    checkmark_Label.config(text = "")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_Button_Clicked():
    global reps
    reps +=1

    work_Sec = WORK_MIN * 60
    short_Break_Sec = SHORT_BREAK_MIN * 60
    long_Break_Sec = LONG_BREAK_MIN * 60
    if(reps % 8 == 0):
        count_Down(long_Break_Sec)  
        timer_Label.config(text = "Break", fg = RED)
    elif(reps % 2 == 0):
        count_Down(short_Break_Sec)  
        timer_Label.config(text = "Break", fg = PINK)
    else:
        count_Down(work_Sec)
        timer_Label.config(text = "Work", fg = GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_Down(count):
    global timer
    count_Min = math.floor(count / 60)
    count_Sec = count % 60
    if count_Sec < 10:
        count_Sec = f"0{count_Sec}"


    canvas.itemconfig(timer_Text, text = f"{count_Min}:{count_Sec}")
    if(count > 0):
        timer = window.after(1000, count_Down, count-1)
    else:
        start_Button_Clicked()
        marks  = ""
        work_Sessions = math.floor(reps/2)
        for _ in range(work_Sessions):
            marks += "✓"
        checkmark_Label.config(text = marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro(aka Tomato)")
window.config(padx=100,pady=50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_Img = PhotoImage(file = "pomodoro-start/tomato.png")
canvas.create_image(100, 112, image = tomato_Img)
timer_Text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME,35,"bold"))
canvas.grid(column = 1, row = 1)

timer_Label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 45))
timer_Label.grid(column = 1, row = 0)

checkmark_Label = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20))
checkmark_Label.grid(column = 1, row = 3)

start_Button = Button(text = "Start", highlightthickness = 0, command = start_Button_Clicked)
start_Button.grid(column = 0, row = 2)

reset_Button = Button(text = "Reset", highlightthickness = 0, command = reset_Button_Pressed)
reset_Button.grid(column = 2, row = 2)

window.mainloop()