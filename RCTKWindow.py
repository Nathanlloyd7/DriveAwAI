#Brings all the individual panels together for one view. Initializes the stage/window etc
from tkinter import *
from RCSpeedPanel import *
from RCMovementPanel import *
from RCVideoPanel import *
class RCTKWindow:
    def __init__(self):
        self.root = Tk() #Makes the window
        self.root.minsize(300,360)
        
        def about():
            about = Toplevel(self.root)
            about.title("About")
            about.minsize(300,300)
            Label(about, text="This is the about Page").grid(row=1, column=0, padx=10, pady=2)
            about.mainloop()

        #menu items
        menuBar = Menu(self.root)
        file = Menu(menuBar, tearoff = 0)
        
        file.add_command(label="Control Settings")
        file.add_command(label="Motor Settings")
        file.add_separator()
        file.add_command(label="Exit", command = self.root.quit)
        menuBar.add_cascade(label = "File", menu = file)

        help = Menu(menuBar, tearoff = 0)
        help.add_command(label="About", command = about)
        menuBar.add_cascade(label="Help", menu = help)
        
        self.root.wm_title("RC App") #Makes the title that will appear in the top left
        self.root.config(background = "Cyan")
        self.leftFrame = Frame(self.root, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)
        self.centralFrame = Frame(self.root, width=200, height = 600)
        self.centralFrame.grid(row=0, column=1, padx=10, pady=2)
        self.leftPanel = RCMovementPanel(self.root, self.leftFrame)
        self.centralFrame = RCVideoPanel(self.root, self.centralFrame)

        self.root.config(menu=menuBar)


    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
