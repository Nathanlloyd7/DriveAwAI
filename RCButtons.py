#buttons class, just using default from tutorial. might make future changes for rollover buttons etc and use throughout
from tkinter import *

class RCButtons:
    def __init__(self, frame, color, callback):
        self.frame = frame
        self.color = color   # the button's color is retained and accessible
        self.callback = callback

        self.button = Button(self.frame, text=self.color.capitalize(),
                            command= lambda: self.callback(self.color) )

#using pack eliminates the need to count grid spaces
        self.button.pack(side=LEFT)