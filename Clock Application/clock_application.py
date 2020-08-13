import time
import tkinter as tk
from tkinter import Label
from time import strftime
import threading


class Gui:
    time_label: tk.Label = None

    def __init__(self, window=None):
        self.window = window
        self.create_stuff()
        t1 = threading.Thread(target=self.update_time)
        t1.start()
        self.window.mainloop()

    def create_stuff(self):
        self.window.title("Clock Application")
        self.window.geometry('900x700')
        self.window.resizable(False, False)
        self.window.configure(background='#E5E5FF')
        l1 = Label(self.window, text="THE TIME IS:", fg="#9999FF", bg='#E5E5FF', font=('Arial', 50))
        l1.pack()

    def update_time(self):
        while True:
            t = strftime('%H:%M:%S %p')
            if self.time_label is None:
                self.time_label = Label(self.window, fg="#9999FF", bg='#E5E5FF', font=('Arial', 25))
                self.time_label.config(text=t)
                self.time_label.pack()
            else:
                self.time_label.config(text=t)
            time.sleep(1)


screen = tk.Tk()
Gui(screen)