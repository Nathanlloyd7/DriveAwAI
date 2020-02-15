#Brings all the individual panels together for one view. Initializes the stage/window etc
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from Code.RCMovementPanel import *
from Code.RCVideoPanel import *
import os
from Code.RCMenuBar import RCMenuBar
from Code.RCPassword import RCPassword

class RCTKWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self) #Makes the window
        dlpath = os.getcwd()
        self.passW = RCPassword()
        self.menubar = RCMenuBar(self)
        self.config(menu=self.menubar)
        self.minsize(950,530)
        self.geometry('950x530+0+0')
        self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file= dlpath+'/Code/Images/realcar1.png'))
        self.wm_title("Drive AwAI") #Makes the title that will appear in the top left
        self.config(background = "Cyan")
        self.leftFrame = Frame(self, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=10)
        self.centralFrame = Frame(self, width=200, height = 600)
        self.centralFrame.grid(row=0, column=1, padx=10, pady=10)
        self.leftPanel = RCMovementPanel(self, self.leftFrame)
        self.centralFrame = RCVideoPanel(self, self.centralFrame)
        

    def start(self):
        self.mainloop() #start monitoring and updating the GUI
