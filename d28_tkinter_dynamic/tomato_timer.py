from tkinter import *
import emoji
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY = "#313543"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")
    label_counter.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    # Count down
    # count_down(5 * 60)
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Long Break", fg="RED")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Short Break", fg="PINK")
    else:
        count_down(work_sec)
        label.config(text="Work", fg="GREEN")

    print(f"Repetition: {reps}")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    if count_min < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # Call a function after waiting
        global timer
        timer = window.after(1000, count_down, count - 1)

    else:
        start_timer()  # Restart if count down to 0

        # Add checkmark
        tomato = emoji.emojize(':thumbs_up:')
        work_reps = math.floor(reps / 2)
        checkmarks = work_reps * tomato
        label_counter.config(text=checkmarks)


# ---------------------------- UI SETUP ------------------------------- #

# Creating a new window and configurations
window = Tk()
window.title("Pomodoro")
window.minsize(width=50, height=50)

# Add some padding (spaces around all widgets)
window.config(padx=100, pady=50)

# Background color of the window
window.config(bg=GREY)

# Create a canvas
canvas = Canvas(width=500, height=500, bg=GREY, highlightthickness=0)
# Add image at the center
tomato_img = PhotoImage(file="mastodon.png")
canvas.create_image(250, 250, image=tomato_img)
# Timer text
timer_text = canvas.create_text(373, 190, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# Title
label = Label(text="Timer", fg=GREEN, bg=GREY, font=("Arial", 30, "bold"))
label.grid(column=2, row=1)

# Call the function when button clicked
button_start = Button(text="Start", command=start_timer, highlightthickness=0)
button_start.grid(column=1, row=3)

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=3, row=3)

# Counter text
label_counter = Label(text="", fg=GREEN, bg=GREY, font=("Arial", 20, "bold"))
label_counter.grid(column=2, row=4)

# Keep the window open
window.mainloop()
