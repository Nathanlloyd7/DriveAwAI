#control direction of rc
from tkinter import *
from RCCar import *
from PIL import Image, ImageTk

class RCMovementPanel:
    def __init__(self, root, frame):
        self.rc = RCCar(True, 50, 50)
        self.root = root
        self.frame = frame
#images import and process into smaller size
        try:
            self.arrowSy = 50   #customizable maybe a menu item?
            self.arrowSx = 50
            self.arrowUp = Image.open("/Images/Arrow-UP.png")
            self.arrowUp = self.arrowUp.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowUp = ImageTk.PhotoImage(self.arrowUp)

            self.arrowUr = Image.open("/Images/Arrow-UR.png")
            self.arrowUr = self.arrowUr.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowUr = ImageTk.PhotoImage(self.arrowUr)

            self.arrowUl = Image.open("/Images/Arrow-UL.png")
            self.arrowUl = self.arrowUl.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowUl = ImageTk.PhotoImage(self.arrowUl)

            self.arrowRi = Image.open("/Images/Arrow-RI.png")
            self.arrowRi = self.arrowRi.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowRi = ImageTk.PhotoImage(self.arrowRi)

            self.arrowLe = Image.open("/Images/Arrow-LE.png")
            self.arrowLe = self.arrowLe.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowLe = ImageTk.PhotoImage(self.arrowLe)

            self.arrowDl = Image.open("/Images/Arrow-DL.png")
            self.arrowDl = self.arrowDl.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowDl = ImageTk.PhotoImage(self.arrowDl)

            self.arrowDo = Image.open("/Images/Arrow-DO.png")
            self.arrowDo = self.arrowDo.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowDo = ImageTk.PhotoImage(self.arrowDo)

            self.arrowDr = Image.open("/Images/Arrow-DR.png")
            self.arrowDr = self.arrowDr.resize((self.arrowSx,self.arrowSy), Image.ANTIALIAS)
            self.arrowDr = ImageTk.PhotoImage(self.arrowDr)

        except:
            print("Something went wrong, File not found")




#Frame for Directional Buttons & speed
        Label(self.frame, text="Direction:").grid(row=0, column=0, padx=10, pady=2)

#top row
        self.topFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.topFrame.grid(row=1, column=0, padx=10, pady=2)
        self.left_upBtn = Button(self.topFrame, text="diag", image=self.arrowUl, command= self.rc.goUpLeft)
        self.left_upBtn.grid(row=1, column=1, padx=10, pady=2)
        self.upBtn = Button(self.topFrame, text="Up",image=self.arrowUp, command= self.rc.goForward)
        self.upBtn.grid(row=1, column=2, padx=10, pady=2)
        self.right_upBtn = Button(self.topFrame, text="diag", image= self.arrowUr, command= self.rc.goUpRight)
        self.right_upBtn.grid(row=1, column=3, padx=10, pady=2)
#Frame to Hold left, stop and right
        self.midFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.midFrame.grid(row=2, column=0, padx=10, pady=2)
        self.leftBtn = Button(self.midFrame, text="Left",image = self.arrowLe, command=self.rc.goLeft)
        self.leftBtn.grid(row=0, column=0, padx=10, pady=2)
        self.stopBtn = Button(self.midFrame, text="Stop", command = self.rc.handbreak)
        self.stopBtn.grid(row=0, column=1, padx=10, pady=2)
        self.rightBtn = Button(self.midFrame, text="Right",image = self.arrowRi, command =self.rc.goRight)
        self.rightBtn.grid(row=0, column=2, padx=10, pady=2)
#Down
        self.botFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.botFrame.grid(row=3, column=0, padx=10, pady=2)
        self.left_downBtn = Button(self.botFrame, text="Diag",image=self.arrowDl, command= self.rc.goBackLeft)
        self.left_downBtn.grid(row=0, column=1, padx=10, pady=2)
        self.downBtn = Button(self.botFrame, text="Down",image=self.arrowDo, command= self.rc.goBack)
        self.downBtn.grid(row=0, column=2, padx=10, pady=2)
        self.right_downBtn = Button(self.botFrame, text="Diag", image=self.arrowDr,command= self.rc.goBackRight)
        self.right_downBtn.grid(row=0, column=3, padx=10, pady=2)
        Label(self.frame, text=" ").grid(row=4, column=0, padx=10, pady=2)
#Auto/Man Toggle
        self.aiTogBtn = Button(self.frame, text="Ai Toggle", command=lambda:print("a/i toggle"))
        self.aiTogBtn.grid(row=5, column=0, padx=10, pady=2)
#speed

        Label(self.frame, text=" ").grid(row=6, column=0, padx=10, pady=2)
        self.speedFrame = Frame(self.frame, width=200, height=10, borderwidth=1)
        self.speedFrame.grid(row=7, column=0, padx=10, pady=2)
        Label(self.speedFrame, text="Speed:").grid(row=0, column=0, padx=10, pady=2)
        self.scale = Scale(self.speedFrame, from_ = 35, to = 100, orient = HORIZONTAL)
        self.scale.grid(row=1, column=0, padx=10, pady=2)
        self.scale.set(75)                                                                           #sets default speed
        self.setSpeed = Button(self.speedFrame, text="Set Speed", command = self.returnSpeed)
        self.setSpeed.grid(row=2, column =0, padx=10, pady=2)

    def returnSpeed(self):
            self.rc.set__spd(self.scale.get())
            print (self.scale.get())     #mock function for now
