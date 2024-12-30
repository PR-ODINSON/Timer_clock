#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time
from threading import Thread

def start_timer():
    try:
        total_seconds = int(hours_var.get()) * 3600 + int(minutes_var.get()) * 60 + int(seconds_var.get())
        if total_seconds <= 0:
            messagebox.showerror("Invalid Input", "Please enter a positive time value.")
            return

        # Disable the Start button during countdown
        start_button.config(state=tk.DISABLED)
        
        def countdown():
            nonlocal total_seconds
            while total_seconds > 0:
                mins, secs = divmod(total_seconds, 60)
                hrs, mins = divmod(mins, 60)
                timer_label.config(text=f"{hrs:02d}:{mins:02d}:{secs:02d}")
                time_elapsed_label.config(text=f"Time Elapsed: {int(hours_var.get())*3600 + int(minutes_var.get())*60 + int(seconds_var.get()) - total_seconds} seconds")
                root.update()
                time.sleep(1)
                total_seconds -= 1

            timer_label.config(text="Time's Up!")
            time_elapsed_label.config(text="Time Elapsed: Complete")
            messagebox.showinfo("Timer", "Time's up!")
            notification.notify(
                title="Countdown Timer",
                message="Time's up!",
                app_name="Countdown Timer",
                timeout=10
            )
            start_button.config(state=tk.NORMAL)

        Thread(target=countdown).start()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main application window
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("450x350")
root.configure(bg="#1c1c1c")

# Variables for time inputs
hours_var = tk.StringVar(value="0")
minutes_var = tk.StringVar(value="0")
seconds_var = tk.StringVar(value="0")

# Header Label
tk.Label(root, text="Countdown Timer", font=("Helvetica", 24, "bold"), fg="#ffffff", bg="#1c1c1c").pack(pady=10)

# Frame for Input Fields
input_frame = tk.Frame(root, bg="#1c1c1c")
input_frame.pack(pady=20)

tk.Label(input_frame, text="Hours:", font=("Helvetica", 14), fg="#ffffff", bg="#1c1c1c").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(input_frame, textvariable=hours_var, width=5, font=("Helvetica", 14)).grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Minutes:", font=("Helvetica", 14), fg="#ffffff", bg="#1c1c1c").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(input_frame, textvariable=minutes_var, width=5, font=("Helvetica", 14)).grid(row=1, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Seconds:", font=("Helvetica", 14), fg="#ffffff", bg="#1c1c1c").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(input_frame, textvariable=seconds_var, width=5, font=("Helvetica", 14)).grid(row=2, column=1, padx=10, pady=5)

# Start Button
start_button = tk.Button(root, text="Start Timer", font=("Helvetica", 16), bg="#4caf50", fg="#ffffff", command=start_timer)
start_button.pack(pady=15)

# Timer Label
timer_label = tk.Label(root, text="00:00:00", font=("Helvetica", 28, "bold"), fg="#ff5722", bg="#1c1c1c")
timer_label.pack(pady=10)

# Time Elapsed Label
time_elapsed_label = tk.Label(root, text="Time Elapsed: 0 seconds", font=("Helvetica", 14), fg="#ffffff", bg="#1c1c1c")
time_elapsed_label.pack(pady=10)

# Run the application
root.mainloop()


# In[ ]:





# In[ ]:




