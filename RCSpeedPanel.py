#Speed panel to edit the speed of the rc.
from tkinter import *

class RCSpeedPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
#Speed Frame
        Label(self.frame, text="Speed:").grid(row=0, column=0, padx=10, pady=2)
        self.slowBtn = Button(self.frame, text="1", command=lambda:print("Speed 0.25%"))
        self.slowBtn.grid(row=1, column=0, padx=10, pady=2)
        self.medBtn = Button(self.frame, text="2", command=lambda:print("Speed 0.50%"))
        self.medBtn.grid(row=2, column=0, padx=10, pady=2)
        self.fastBtn = Button(self.frame, text="3", command=lambda:print("Speed 0.75%"))
        self.fastBtn.grid(row=3, column=0, padx=10, pady=2)
        self.offBtn = Button(self.frame, text="Handbreak", command=lambda:print("Hand Break"))
        self.offBtn.grid(row=4, column=0, padx=10, pady=2)