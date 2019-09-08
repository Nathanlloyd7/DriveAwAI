#control direction of rc
from tkinter import *

class RCDirectionPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

#Centra Frame for Directional Buttons
        Label(self.frame, text="Direction:").grid(row=0, column=0, padx=10, pady=2)

#Up
        self.upBtn = Button(self.frame, text="Up", command=lambda:print("up"))
        self.upBtn.grid(row=1, column=0, padx=10, pady=2)

#Frame to Hold left and right
        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=2, column=0, padx=10, pady=2)
        self.leftBtn = Button(self.btnFrame, text="Left", command=lambda:print("left"))
        self.leftBtn.grid(row=0, column=0, padx=10, pady=2)
        self.rightBtn = Button(self.btnFrame, text="Right", command=lambda:print("right"))
        self.rightBtn.grid(row=0, column=1, padx=10, pady=2)

#Down
        self.downBtn = Button(self.frame, text="Down", command=lambda:print("down"))
        self.downBtn.grid(row=3, column=0, padx=10, pady=2)

        Label(self.frame, text=" ").grid(row=4, column=0, padx=10, pady=2)
#Auto/Man Toggle

        self.aiTogBtn = Button(self.frame, text="Ai Toggle", command=lambda:print("a/i toggle"))
        self.aiTogBtn.grid(row=5, column=0, padx=10, pady=2)