import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rept = 0
timer=None



window = Tk()
window.title("Pomodro")
window.config(padx=100,pady=50,bg=YELLOW)

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(canvas_timer, text="00:00")
    label_title.config(text="Timer")
    label_check.config(text="")
    global rept
    rept = 0


def start_counter():
    global rept
    rept += 1
    WORK_MIN_sec = WORK_MIN*60
    SHORT_BREAK_MIN_sec = SHORT_BREAK_MIN*60
    LONG_BREAK_MIN_sec = LONG_BREAK_MIN*60


    if rept % 8 == 0:
        counter(LONG_BREAK_MIN_sec)
        label_title.config(text="Break", fg=RED)
    elif rept % 2 ==0:
        counter(SHORT_BREAK_MIN_sec)
        label_title.config(text="break", fg=PINK)
    else:
        counter(WORK_MIN_sec)
        label_title.config(text="Work", fg=GREEN)


def counter(count):
    count_minute = math.floor(count/60)
    cont_sec = count%60

    if cont_sec < 10:
        cont_sec = f"0{cont_sec}"
    canvas.itemconfig(canvas_timer, text=f"{count_minute}:{cont_sec}")





    if count > 0:
        global timer
        timer = window.after(1000,counter, count -1)
    else:
        start_counter()

        marks =""
        work_session = math.floor(rept/2)
        for _ in range(work_session):
            marks += "✔"
            label_check.config(text=marks)



label_title = Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50, "bold"))
label_title.grid(row=0,column=1)

canvas = Canvas(width=400,height=448,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(200,200,image=tomato_image)
canvas_timer = canvas.create_text(200,224,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)



button_start = Button(text="start",highlightthickness=0,command=start_counter)
button_start.grid(row=2,column=0)


label_check = Label(fg=GREEN,bg=YELLOW)
label_check.grid(row=3,column=1)

button_end= Button(text="Reset",highlightthickness=0,command=reset_timer)
button_end.grid(row=2,column=2)


window.mainloop()