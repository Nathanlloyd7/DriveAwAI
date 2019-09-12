#Speed panel to edit the speed of the rc.
#12/08/19
import explorerhat 
from tkinter import *


class RCSpeedPanel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame
#Speed Frame
        Label(self.frame, text="Speed:").grid(row=0, column=0, padx=10, pady=2)
        self.slowBtn = Button(self.frame, text="1", command= speed1)
        self.slowBtn.grid(row=1, column=0, padx=10, pady=2)
        self.medBtn = Button(self.frame, text="2", command=speed2 )
        self.medBtn.grid(row=2, column=0, padx=10, pady=2)
        self.fastBtn = Button(self.frame, text="3", command = speed3)
        self.fastBtn.grid(row=3, column=0, padx=10, pady=2)
        self.offBtn = Button(self.frame, text="Handbreak", command=lambda:print("Hand Break"))
        self.offBtn.grid(row=4, column=0, padx=10, pady=2)
        
global speedint
speedint = 100
def speed1():
    explorerhat.motor.one.forwards(speedint *0.333)
    explorerhat.motor.two.forward(speedint *0.333)
    
def speed2():
    explorerhat.motor.one.forwards(75)    #so updating speed like this is wrong
    explorerhat.motor.two.forward(75)     #if i do like this then it will make it go  
    
def speed3():
    explorerhat.motor.one.forwards(speedint ) #wereas i just want a var to be updated
    explorerhat.motor.two.forward(speedint )
    
