#Brings all the individual panels together for one view. Initializes the stage/window etc
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from RCMovementPanel import *
from RCVideoPanel import *
import os
from RCMenuBar import RCMenuBar
class RCTKWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #Makes the window
        menubar = RCMenuBar(self)
        self.config(menu=menubar)
        self.minsize(300,360)
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file='realcar1.png'))
        self.wm_title("RC App") #Makes the title that will appear in the top left
        self.config(background = "Cyan")
        self.leftFrame = Frame(self, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)
        self.centralFrame = Frame(self, width=200, height = 600)
        self.centralFrame.grid(row=0, column=1, padx=10, pady=2)
        self.leftPanel = RCMovementPanel(self, self.leftFrame)
        self.centralFrame = RCVideoPanel(self, self.centralFrame)


    def start(self):
        self.mainloop() #start monitoring and updating the GUI
