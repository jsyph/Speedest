from playsound import playsound
from renit import reinit_app
from shape_creators import *
from testbrain import TestBrain

from tkinter import ttk
from ttkthemes import ThemedTk
import math

REC_WIDTH = 600
REC_HEIGHT = 200

RECTANGLE_COLOUR = "#3fc1c9"
RECTANGLE_TEXT_COLOUR = "#364f6b"
BACKGROUND_COLOUR = "#f5f5f5"
RED = "#fc5185"
YELLOW = "#ffde7d"
WIDGET_WIDTH = 95
font_data = ("TkMenuFont", 20, "normal")
window = ThemedTk(theme="adapta")
window.title("Speedest")
window.config(padx=100, pady=100, background=BACKGROUND_COLOUR)
brain = TestBrain()


# ----------------------------------------------------------------------------------------------------------------------


def show_time(event):
    time = str(math.ceil(float(scale_variable.get())))
    time_val_label.config(text=f"{time}s")


def start_test():
    playsound("sounds/select_sound.mp3", block=False)
    controlls_frame.grid_remove()
    test_frame.grid(row=1, column=0, pady=(20, 0))
    test_entery.focus()

    brain.get_scentence()
    test_text_canvas.itemconfig(test_text, text=brain.scentence)
    print(math.ceil(float(scale_variable.get())))
    brain.difficulty_time = math.ceil(float(scale_variable.get()))
    brain.start_timer()


def change_text(event):
    brain.check_timer()
    if event.keysym == "space":
        brain.get_scentence()
        test_text_canvas.itemconfig(test_text, text=brain.scentence)
        if brain.is_test_complete["state"]:
            window.focus_set()
            test_entery.grid_remove()
            show_result_btn.grid(row=2, column=0)
            brain.end_timer()
            test_entery_label.config(text=brain.is_test_complete["message"])
            test_text_canvas.itemconfig(test_text, text=brain.is_test_complete["message"])
        else:
            brain.index += 1
            brain.words_left -= 1
            test_entery_label.config(text=f"{str(brain.words_left)} words left")


def show_result():
    playsound("sounds/select_sound.mp3", block=False)
    window.focus_set()
    brain.check_answer(str(test_entery.get()))
    test_frame.grid_remove()
    test_text_canvas.grid_remove()
    test_result_frame.grid(row=0, column=0)
    title_canvas.itemconfig(title_text, text=brain.is_test_complete["message"])
    errors_canvas.itemconfig(errors_text, text=f"{brain.user_score['errors']} wrong words.")
    speed_canvas.itemconfig(speed_text, text=f"{brain.user_score['typing_speed']} words/second")


def go_home():
    reinit_app(window)


# ----------------------------------------------------------------------------------------------------------------------
# Create Canvas that contains the rectabgle and the test text
test_text_canvas = tk.Canvas(window, width=REC_WIDTH, height=REC_HEIGHT, background=BACKGROUND_COLOUR,
                             highlightthickness=0)
rec = round_rectangle(test_text_canvas, 0, 0, REC_WIDTH, REC_HEIGHT, radius=50, fill=RECTANGLE_COLOUR,
                      width=test_text_canvas.winfo_width())
test_text = test_text_canvas.create_text(REC_WIDTH / 2, REC_HEIGHT / 2, fill=RECTANGLE_TEXT_COLOUR,
                                         font=f"{'Futura'} {font_data[1]} {'bold'}",
                                         text="Welcome to Speedy")
test_text_canvas.grid(row=0, column=0)
# ----------------------------------------------------------------------------------------------------------------------
# The controls of the start window
controlls_frame = ttk.Frame(window)

scale_variable = tk.DoubleVar()
difficulty_frame = ttk.Frame(controlls_frame)

difficulty_label = ttk.Label(difficulty_frame, text="Choose test time:", font=("Futura", 10, "normal"))
time_val_label = ttk.Label(difficulty_frame, font=("Futura", 8, "normal"))
difficulty_scale = ttk.Scale(difficulty_frame, variable=scale_variable, length=REC_WIDTH - 140, orient=tk.HORIZONTAL,
                             from_=10, to=180, command=show_time)
difficulty_scale.set(60)

difficulty_label.grid(row=0, column=0)
difficulty_scale.grid(row=0, column=1, padx=(10, 0))
time_val_label.grid(row=0, column=2)

difficulty_frame.grid(row=1, column=0, pady=(20, 0))

start_button = ttk.Button(controlls_frame, width=WIDGET_WIDTH, text="Start Test", command=start_test)
start_button.grid(row=2, column=0, pady=(20, 0))

controlls_frame.grid(row=1, column=0, pady=(20, 0))

# ----------------------------------------------------------------------------------------------------------------------
test_frame = ttk.Frame(window)
test_entery_label = ttk.Label(test_frame, text="Start typing the words above.", font=(font_data[0], 10, font_data[2]))
test_entery = ttk.Entry(test_frame, width=WIDGET_WIDTH)
test_entery.bind("<KeyPress>", change_text)
show_result_btn = ttk.Button(test_frame, width=WIDGET_WIDTH, text="Show results", command=show_result)

test_entery_label.grid(row=0, column=0)
test_entery.grid(row=1, column=0)
# ----------------------------------------------------------------------------------------------------------------------
REC_HEIGHT = REC_HEIGHT
REC_WIDTH = REC_WIDTH
small_rec_width = REC_WIDTH / 2
font = "Futura 20 bold"
test_result_frame = ttk.Frame(window)

# Button to home
home_btn = ttk.Button(test_result_frame, command=go_home, text="Redo Test", width=100)

# Title canvas that displays the brain.is_test_complete["message"]
title_canvas = tk.Canvas(test_result_frame, width=REC_WIDTH, height=REC_HEIGHT,
                         background=BACKGROUND_COLOUR,
                         highlightthickness=0)
title_rec = round_rectangle(title_canvas, 0, 0, REC_WIDTH, REC_HEIGHT, radius=50,
                            fill=RECTANGLE_COLOUR,
                            width=REC_WIDTH)
title_text = title_canvas.create_text(REC_WIDTH / 2, REC_HEIGHT / 2,
                                      fill=RECTANGLE_TEXT_COLOUR,
                                      font=font)

# Errors canvas that displays the brain.user_score["errors"]
errors_canvas = tk.Canvas(test_result_frame, width=small_rec_width, height=REC_HEIGHT,
                          background=BACKGROUND_COLOUR,
                          highlightthickness=0)
errors_rec = round_rectangle(errors_canvas, 0, 0, small_rec_width, REC_HEIGHT, radius=50,
                             fill=RED,
                             width=small_rec_width)
errors_text = errors_canvas.create_text(small_rec_width / 2, REC_HEIGHT / 2,
                                        fill=RECTANGLE_TEXT_COLOUR,
                                        font=font)

# Speed canvas which displayes the brain.user_score["typing_speed"]
speed_canvas = tk.Canvas(test_result_frame, width=small_rec_width, height=REC_HEIGHT,
                         background=BACKGROUND_COLOUR,
                         highlightthickness=0)
speed_rec = round_rectangle(speed_canvas, 0, 0, small_rec_width, REC_HEIGHT, radius=50,
                            fill=YELLOW,
                            width=small_rec_width)
speed_text = speed_canvas.create_text(small_rec_width / 2, REC_HEIGHT / 2,
                                      fill=RECTANGLE_TEXT_COLOUR,
                                      font=font)
title_canvas.grid(row=0, column=0, columnspan=2)
errors_canvas.grid(row=1, column=0)
speed_canvas.grid(row=1, column=1)
home_btn.grid(row=2, column=0, columnspan=2)

# ----------------------------------------------------------------------------------------------------------------------
window.mainloop()
