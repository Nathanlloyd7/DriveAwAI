#rc car class
from time import sleep
import explorerhat

class RCCar:
    def __init__(self, manual, mot1_spd, mot2_spd):
        self.manual = True
        self.mot1_spd = 50
        self.mot2_spd = 50

    def motors_spd_toStr(self):
        mot1print = str(self.mot1_spd) #change this from (1,2) to (L,R)?
        mot2print = str(self.mot2_spd)
        return ("Motor1: " + mot1print + "\nMotor2: "+ mot2print)

    def goForward(self):
        explorerhat.motor.one.forwards(self.mot1_spd)
        explorerhat.motor.two.forward(self.mot2_spd)


    def handbreak(self):
        explorerhat.motor.one.stop()
        explorerhat.motor.two.stop()

    def goBack(self):
        explorerhat.motor.one.backwards(50)
        explorerhat.motor.two.backward(50)


    # May need fine tuning
    def goRight(self):
        explorerhat.motor.one.forward(50)
        explorerhat.motor.two.backward(50)

    def goLeft(self):
        explorerhat.motor.two.forward(50)
        explorerhat.motor.one.backward(50)

    def goUpRight(self):
        explorerhat.motor.one.forward(70)
        explorerhat.motor.two.forward(40)

    def goUpLeft(self):
        explorerhat.motor.one.forward(40)
        explorerhat.motor.two.forward(70)

    def goBackRight(self):
        explorerhat.motor.one.backwards(70)
        explorerhat.motor.two.backward(40)

    def goBackLeft(self):
        explorerhat.motor.one.backwards(40)
        explorerhat.motor.two.backward(70)

    def set__spd(self, newspeed):        #another method of setting speed
        self.mot1_spd = newspeed                      #would only need one method but
        self.mot2_spd = newspeed                    #would need to pass ints in param
