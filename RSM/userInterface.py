import tkinter as tk

LARGE_FONT = ("Verdana", 12)

class UserInterfacePrototype(tk.Tk):
    """Base code for the user interface application"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, NewResumePage, LoadFilePage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "RSM Manager", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "New Resume",
                            command = lambda : controller.show_frame(NewResumePage))
        button1.pack()

        button2 = tk.Button(self, text = "Load Resume",
                            command = lambda : controller.show_frame(LoadFilePage))
        button2.pack()

class NewResumePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="New Resume", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        button1 = tk.Button(self, text="Cancel",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class LoadFilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Load File", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)


app = UserInterfacePrototype()
app.title("RSM Manager (User Interface Prototype)")
app.mainloop()