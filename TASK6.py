import tkinter as tk
import time
from tkinter import messagebox

def update_timer():
    if time_left.get() > 0:
        time_left.set(time_left.get() - 1)
        label.config(text=str(time_left.get()))
        root.after(1000, update_timer)
    else:
        messagebox.showinfo("Time's up!", "The countdown has finished!")

def start_timer():
    try:
        time_left.set(int(entry.get()))
        entry.delete(0, tk.END)
        update_timer()
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer")

root = tk.Tk()
root.title("Countdown Timer")

time_left = tk.IntVar()

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter time in seconds:", font=("Helvetica, 14"))
label.pack(pady=5)

entry = tk.Entry(frame, font=("Helvetica, 14"))
entry.pack(pady=5)

start_button = tk.Button(frame, text="Start Timer", command=start_timer, font=("Helvetica, 14"))
start_button.pack(pady=20)

time_display = tk.Label(frame, textvariable=time_left, font=("Helvetica, 48"))
time_display.pack(pady=20)

root.mainloop()
