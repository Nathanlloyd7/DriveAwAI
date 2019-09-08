#view the live video from the picamera
from tkinter import *
from RCButtons import *

class RCVideoPanel:
    #As I've been adapting code from a tkinter tutorial and have not tried using open cv yet for video streaming into the gui
    #I will be leaving this panel as is, this is the only class that uses the RCButtons class which is displayed in the tutorial
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

		#Right Frame and its contents/ needs biggest edit open cv for video
        self.circleCanvas = Canvas(self.frame, width=100, height=100, bg='white')
        self.circleCanvas.grid(row=0, column=0, padx=10, pady=2)

        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)


        self.redBtn = RCButtons(self.btnFrame, "red", self.makeCircle)
        self.yellowBtn = RCButtons(self.btnFrame, "yellow", self.makeCircle)
        self.greenBtn = RCButtons(self.btnFrame, "green", self.makeCircle)

        self.colorLog = Text(self.frame, width = 30, height = 10, takefocus=0)
        self.colorLog.grid(row=3, column=0, padx=10, pady=2)

    def makeCircle(self, color):
        self.circleCanvas.create_oval(20, 20, 80, 80, width=0, fill=color)
        self.colorLog.insert(0.0, color.capitalize() + "\n")