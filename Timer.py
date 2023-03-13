from tkinter import *
import time

root = Tk()
root.title("Timer")
root.geometry("300x200")

time_var = StringVar()
time_var.set("00:00:00")

time_label = Label(root, textvariable=time_var, font=("Helvetica", 48))
time_label.pack(pady=20)

start_button = Button(root, text="Start", font=("Helvetica", 14))
start_button.pack(side=LEFT, padx=10)

stop_button = Button(root, text="Stop", font=("Helvetica", 14))
stop_button.pack(side=RIGHT, padx=10)

def start_timer():
    global running
    running = True
    start_time = time.time()
    while running:
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(elapsed_time, 60)
        hours, minutes = divmod(minutes, 60)
        time_str = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"
        time_var.set(time_str)
        root.update()
        time.sleep(0.01)

def stop_timer():
    global running
    running = False

start_button.config(command=start_timer)
stop_button.config(command=stop_timer)

root.mainloop()
