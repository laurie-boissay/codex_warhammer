import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.background_color = "#0C090A"   #grey
        self.title_color = "#FFEBCD"        #parchment
        self.letter_color = "cyan"     
        self.other_color = "#00FF00"        #green
        self.board_color ="#6F4E37"         #brown
        
        #self.my_frame(self.winfo_screenwidth(), self.winfo_screenheight())
        self.pack()
        self.create_widgets()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        # Create the application variable.
        self.contents = tk.StringVar()
        # Set it to some value.
        self.contents.set("Puissance de l'armée.")
        # Tell the entry widget to watch this variable.
        self.entrythingy["textvariable"] = self.contents

        # Define a callback for when the user hits return.
        # It prints the current value of the variable.
        self.entrythingy.bind('<Key-Return>',
                             self.print_contents)

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Liste d'armée Blood Angels :"
        self.hi_there["command"] = self.say_text
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def print_contents(self, event):
        print("La puissance de l'armée sera :",
              self.contents.get())

    def say_text(self, text):
        print(text)
	
# Display window.
    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Codex Warhammer Blood Angels")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    app.master.minsize(round(width/2), round(height/2))
    app.master.maxsize(width, height)
    app.mainloop()