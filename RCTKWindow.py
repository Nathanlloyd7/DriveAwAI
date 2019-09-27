#Brings all the individual panels together for one view. Initializes the stage/window etc
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from RCMovementPanel import *
from RCVideoPanel import *
import os
class RCTKWindow:
    def __init__(self):
        self.root = tk.Tk() #Makes the window
        self.root.minsize(300,360)
        self.root.tk.call('wm', 'iconphoto', self.root._w, tk.PhotoImage(file='realcar1.png'))

        #menu functions
        def controlsetting():  #will allow customization
            controlSet = Toplevel(self.root)
            controlSet.title("Control Panel")
            controlSet.minsize(300,300)
            Label(controlSet, text="This is the Control Page").grid(row=0, column=1, padx=10, pady=2)
            controlSet.mainloop()

        def motorsetting():  #will allow customization
            motorSetsFile = open("motorSetting.txt", "w+") #current setup lets you save to a doc but not show in a log or print in??
            while True:
                loadedVar = motorSetsFile.read(1)
                break
            print(str(loadedVar))
            
            def saveMotor(motorSetsFile):
                print("saved" + str(selected.get()))
                motorSetsFile.write(str(selected.get()))
                motorSetsFile.close()
                motorSet.destroy()

            motorSet = Toplevel(self.root)
            motorSet.title("Motor Control Panel")
            motorSet.minsize(300,300)
            Label(motorSet, text="Here you can toggle whether manual speed control is active").grid(row=0, column=0, padx=10, pady=2)
            Label(motorSet, text=" ").grid(row=1, column=1, padx=10, pady=2)
            Label(motorSet, text="Would you like to toggle manual speed?:").grid(row=2, column=0, padx=10, pady=2) #replace 'off' with a loaded in var %
            motorFrame = Frame(motorSet, width=200, height=10, borderwidth=1)
            motorFrame.grid(row=3, column=0, padx=10, pady=2)
            selected = IntVar()
            radioOn = Radiobutton(motorFrame, text="On", value=1, variable=selected).grid(row=0, column=0, padx=10, pady=2)
            radioOff = Radiobutton(motorFrame, text="Off",value=0, variable=selected).grid(row=0, column=1, padx=10, pady=2)
            saveLock = Button(motorSet, text="Save", command = lambda:saveMotor(motorSetsFile)).grid(row=4, column=0, padx=10, pady=2)
            stateLog = Text(motorSet, width = 20, height = 2, takefocus=0)
            stateLog.grid(row=5, column=0, padx=10, pady=2)
            stateLog.insert(0.0,"1 is On, 0 is Off\nCurrent state: "+ loadedVar)
            motorSet.mainloop()


        def about():
            messagebox.showinfo("About", """Hello, welcome to this RC application\n
            This application will function as a minature version of a real full size car, giving the user the ability to control it using GUI or keyboard inputs as well as toggle assistive driving technologies:\n
            If you have any questions please contact N Lloyd here:\n P16187037@my365.dmu.ac.uk""")




        #menu items
        menuBar = Menu(self.root)
        file = Menu(menuBar, tearoff = 0)
        file.add_command(label="Control Settings", command = controlsetting)
        file.add_command(label="Motor Settings", command = motorsetting)
        file.add_separator()
        file.add_command(label="Exit", command = self.root.destroy)
        menuBar.add_cascade(label = "File", menu = file)
        help = Menu(menuBar, tearoff = 0)
        help.add_command(label="About", command = about)
        menuBar.add_cascade(label="Help", menu = help)




        self.root.wm_title("RC App") #Makes the title that will appear in the top left
        self.root.config(background = "Cyan")
        self.leftFrame = Frame(self.root, width=200, height = 600)
        self.leftFrame.grid(row=0, column=0, padx=10, pady=2)
        self.centralFrame = Frame(self.root, width=200, height = 600)
        self.centralFrame.grid(row=0, column=1, padx=10, pady=2)
        self.leftPanel = RCMovementPanel(self.root, self.leftFrame)
        self.centralFrame = RCVideoPanel(self.root, self.centralFrame)
        self.root.config(menu=menuBar)


    def start(self):
        self.root.mainloop() #start monitoring and updating the GUI
