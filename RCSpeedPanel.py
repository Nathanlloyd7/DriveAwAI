#Speed panel to edit the speed of the rc.
#12/09/19
from RCCar import *
from tkinter import *


class RCSpeedPanel:
    def __init__(self, root, frame):
        rc = RCCar(True, 50, 50)
        self.root = root
        self.frame = frame
#Speed Frame
        Label(self.frame, text="Speed:").grid(row=0, column=0, padx=10, pady=2)
        self.slowBtn = Button(self.frame, text="1", command= rc.set_low_spd)
        self.slowBtn.grid(row=1, column=0, padx=10, pady=2)
        self.medBtn = Button(self.frame, text="2", command= rc.set_med_spd )
        self.medBtn.grid(row=2, column=0, padx=10, pady=2)
        self.fastBtn = Button(self.frame, text="3", command = rc.set_high_spd)
        self.fastBtn.grid(row=3, column=0, padx=10, pady=2)
        self.offBtn = Button(self.frame, text="Handbreak", command=lambda:print(rc.motors_spd_toStr()))
        self.offBtn.grid(row=4, column=0, padx=10, pady=2)
    


