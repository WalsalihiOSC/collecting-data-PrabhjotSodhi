import tkinter as tk

class Root(object):
    """
    A single instance of this class is responsible for 
    managing which individual window state is active
    and keeping it updated.
    """
    def __init__(self, master):
        self.master = master
        self.master.geometry('300x300')
        self.master.title("Week 8 Tasks")
        self.frame = tk.Frame(self.master)
        self.frame.pack()
    def change_state(self, states, state_to, frame=None):
        self.frame.destroy()
        if frame is not None:
            frame.destroy()
        self.frame = tk.Frame(self.master)
        self.frame.pack(expand=tk.TRUE)
        states[state_to](self.frame)