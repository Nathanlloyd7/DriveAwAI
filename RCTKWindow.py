#Brings all the individual panels together for one view. Initializes the stage/window etc
from tkinter import *
from RCSpeedPanel import *
from RCDirectionPanel import *
from RCVideoPanel import *
class RCTKWindow:
    def __init__(self):
        self.root = Tk() #Makes the window
        self.root.wm_title("RC App") #Makes the title that will appear in the top left
        self.root.config(background = "Cyan")
        self.leftFrame = Frame(self.root, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)
        self.centralFrame = Frame(self.root, width=200, height = 600)
        self.centralFrame.grid(row=0, column=1, padx=10, pady=2)
        self.rightFrame = Frame(self.root, width=200, height = 300)
        self.rightFrame.grid(row=0, column=2, padx=10, pady=2)
        self.leftPanel = RCSpeedPanel(self.root, self.leftFrame)
        self.centralFrame = RCDirectionPanel(self.root, self.centralFrame)
        self.rightPanel = RCVideoPanel(self.root, self.rightFrame)

    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
