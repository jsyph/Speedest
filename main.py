from tkinter import ttk
from ttkthemes import ThemedTk
from shape_creators import *
import math
from time import sleep
from testbrain import TestBrain

REC_WIDTH = 600
REC_HEIGHT = 200

RECTANGLE_COLOUR = "#3fc1c9"
RECTANGLE_TEXT_COLOUR = "#364f6b"
BACKGROUND_COLOUR = "#f5f5f5"
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
    controlls_frame.grid_remove()
    test_text_canvas.itemconfig(test_text, text="Starting....")
    test_entery_label.grid(row=1, column=0, pady=(20, 0), padx=(0, 20))
    test_entery.grid(row=2, column=0)

    brain.get_scentence()
    test_text_canvas.itemconfig(test_text, text=brain.scentence)


def change_text(event: tk.Event):
    if event.keysym == "space":
        brain.get_scentence()
        test_text_canvas.itemconfig(test_text, text=brain.scentence)
        brain.index += 1


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
test_entery_label = ttk.Label(window, text="Start typing the words above.", font=(font_data[0], 10, font_data[2]))
test_entery = ttk.Entry(window, width=WIDGET_WIDTH)
test_entery.bind("<KeyPress>", change_text)
# ----------------------------------------------------------------------------------------------------------------------
window.mainloop()
