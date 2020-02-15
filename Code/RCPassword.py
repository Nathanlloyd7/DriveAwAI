import time
import explorerhat as hat
import RPi.GPIO as GPIO
import sys
import os



class RCPassword:
    def __init__(self):
        dlpath = os.getcwd()
        #loadinpin
        loadedFile = open(dlpath+"/Code/Settings/passSetting.txt", "r")
        loadedPW = loadedFile.read()
        loadedFile.close()
        #print(loadedPW.split(','))
        loadedPW0 = int(loadedPW[0])
        loadedPW1 = int(loadedPW[1])
        loadedPW2 = int(loadedPW[2])
        loadedPW3 = int(loadedPW[3])


        #check password is in range
        if (loadedPW0+loadedPW1+loadedPW2+loadedPW3) < 4 or (loadedPW0+loadedPW1+loadedPW2+loadedPW3) >16:
            print("The values exceed pin range, passwords have been tampered with")
            sys.exit()
        else:
            pass

        self.correct_pin = [loadedPW0,loadedPW1,loadedPW2,loadedPW3]
        self.pin = []
        self.counter = 1

        #Visual Initialize
        hat.output.one.on()  ## Turns green LED on
        time.sleep(0.1)
        hat.output.one.off()  ## Turns green LED off
        time.sleep(0.1)
        hat.output.two.on()  ## Turns green LED on
        time.sleep(0.1)
        hat.output.two.off()  ## Turns green LED off
        time.sleep(0.1)
        hat.output.one.on()  ## Turns green LED on
        time.sleep(0.2)
        hat.output.one.off()  ## Turns green LED off
        time.sleep(0.2)
        hat.output.two.on()  ## Turns green LED on
        time.sleep(0.2)
        hat.output.two.off()  ## Turns green LED off
        time.sleep(0.2)
        #print(self.correct_pin)


        while True:
            while len(self.pin) < 4:  ## Keeping adding until 4 digits added
                hat.touch.pressed(self.add_to_pin)
                time.sleep(0.05)
            if self.pin == self.correct_pin:  ## Runs with correct PIN
                print('PIN correct!')
                for i in range(5):  ## Blinks LEDs
                    hat.output.one.on()  ## Turns green LED on
                    time.sleep(0.1)
                    hat.output.one.off()  ## Turns green LED off
                    time.sleep(0.1)
                    break
                break

            elif self.counter < 3:  ## Runs with incorrect PIN
                print('PIN incorrect! Try again.')
                print(self.counter, " out of 3 attempts")
                self.counter = self.counter +1
                for i in range(5):   ## Blinks LEDs
                    hat.output.two.on()  ## Turns red LED on
                    time.sleep(0.1)
                    hat.output.two.off()  ## Turns red LED off
                    time.sleep(0.1)
            else:
                print("too many attempts, no access")
                sys.exit()


            self.pin = []  ## Resets the list after 4 digits have been entered


    def add_to_pin(self, channel, event):
        if channel > 4:  ## Only use channels 1-4
            return
        if event == 'press':
            global pin
            self.pin.append(channel)
            hat.light[channel-1].on()  ## Blink the corresponding LED
            time.sleep(0.05)
            hat.light[channel-1].off()

    def setPin(self):
        p1= int(input("Please enter first number\n"))
        p2=int(input("Please enter first number\n"))
        p3=int(input("Please enter first number\n"))
        p4=int(input("Please enter first number\n"))
        self.correct_pin = [p1,p2,p3,p4]

    def getSavedPin(self):
        return self.correct_pin

