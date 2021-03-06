import tkinter as tk
from window import Root

class DataCollectGUI:
    def __init__(self):
        self.backend = DataCollectBackend()
        print("hello")
    def enter_data_state(self, frame):
        top_frame = tk.Frame(frame, bg='TOMATO')
        collect_label = tk.Label(top_frame, text='Collecting Person Data', bg='TOMATO')
        change_state_button = tk.Button(top_frame, text='Show Data', command=lambda: window.change_state(states, 'SHOW_DATA', top_frame))

        collect_label.grid(row=0, column=0, padx=20, pady=20)
        change_state_button.grid(row=0, column=1, padx=20, pady=20)
        top_frame.grid(row=0, column=0, columnspan=2)

        context_frame = tk.Frame(frame)
        tk.Label(context_frame, text="First Name:").grid()
        tk.Label(context_frame, text="Age:").grid()
        tk.Label(context_frame, text="Do you have mobile:").grid()
        context_frame.grid(row=1, column=0, padx=10, pady=20)

        entry_display_frame = tk.Frame(frame)
        name_entry = tk.Entry(entry_display_frame, textvariable=self.backend.name_var)
        age_entry = tk.Entry(entry_display_frame, textvariable=self.backend.age_var)
    
        name_entry.grid(columnspan=2)
        age_entry.grid(columnspan=2)
        entry_display_frame.grid(row=1, column=1, columnspan=2, padx=10, pady=20)
        
        tk.Radiobutton(entry_display_frame, var=self.backend.phone_var, value=True, text="Yes").grid(row=2, column=0)
        tk.Radiobutton(entry_display_frame, var=self.backend.phone_var, value=False, text="No").grid(row=2, column=1)
        tk.Button(entry_display_frame, text="Add person", command=lambda: self.backend.add_person(self.backend.name_var.get(), self.backend.age_var.get(), self.backend.phone_var.get())).grid(row=3, column=0)

    def show_data_state(self, frame):
        top_frame = tk.Frame(frame, bg='TOMATO')
        collect_label = tk.Label(top_frame, text='Collecting Person Data', bg='TOMATO')
        change_state_button = tk.Button(top_frame, text='Collect Data', command=lambda: window.change_state(states, 'ENTER_DATA', top_frame))

        collect_label.grid(row=0, column=0, padx=20, pady=20)
        change_state_button.grid(row=0, column=1, padx=20, pady=20)
        top_frame.grid(row=0, column=0, columnspan=2)

        context_frame = tk.Frame(frame)
        name, age, phone = self.backend.get_person()[0], self.backend.get_person()[1], self.backend.get_person()[2]
        self.name_l = tk.Label(context_frame, text=f"First Name: {name}")
        self.name_l.grid()
        self.age_l = tk.Label(context_frame, text=f"Age: {age}")
        self.age_l.grid()
        self.phone_l = tk.Label(context_frame, text=f"{name} {phone}")
        self.phone_l.grid()
        context_frame.grid(row=1, column=0, padx=10, pady=20)

        controls_frame = tk.Frame(frame)
        controls_frame.grid(row=2, column=0, columnspan=2)
        tk.Button(controls_frame, text="Previous", command=lambda: self.update_date(False)).pack(side=tk.LEFT)
        tk.Button(controls_frame, text="Next", command=lambda: self.update_date(True)).pack(side=tk.RIGHT)
    def update_date(self, bRight):
        self.backend.cycle_person(bRight)
        name, age, phone = self.backend.get_person()[0], self.backend.get_person()[1], self.backend.get_person()[2]
        self.name_l.configure(text=f"First Name: {name}")
        self.age_l.configure(text=f"Age: {age}")
        self.phone_l.configure(text=f"{name} {phone}")



class DataCollectBackend:
    def __init__(self):
        self.people = []
        self.name_var, self.age_var, self.phone_var = tk.StringVar(), tk.StringVar(), tk.BooleanVar()
        self.index = 0
    def add_person(self, name, age, phone):
        if phone == True:
            phone = "has a mobile phone"
        else:
            phone = "doesn't have a mobile phone"
        self.people.append((name,age,phone))
    def cycle_person(self, bRight):
        print(self.index)
        if bRight:
            if self.index == len(self.people)-1:
                self.index = 0
            else:
                self.index += 1
        else:
            if self.index == 0:
                self.index = len(self.people)-1
            else:
                self.index -= 1
        self.name = self.people[self.index][0]
        self.age = self.people[self.index][1]
        self.phone = self.people[self.index][2]
    def get_person(self):
        if self.index == 0:
            return self.people[0]
        else:
            return (self.name, self.age, self.phone)

if __name__ == '__main__':
    root = tk.Tk()
    GUI = DataCollectGUI()
    states = {"ENTER_DATA": GUI.enter_data_state, "SHOW_DATA": GUI.show_data_state}
    window = Root(root)
    window.change_state(states, 'ENTER_DATA')
    root.mainloop()
    