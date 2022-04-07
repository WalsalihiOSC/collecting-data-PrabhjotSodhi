import tkinter as tk

class DataCollectGUI:
    def __init__(self):
        main_frame = tk.Frame(root)
        main_frame.pack()
        self.backend = DataCollectBackend()

class DataCollectBackend:
    def __init__(self):
        data = []
        person = []
        first_name_var = tk.StringVar()
        last_name_var = tk.StringVar()
        mobile_phone_var = tk.BooleanVar()

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('250x250')
    root.title("Collecting Data Task")
    DataCollectBackend()
    root.mainloop()