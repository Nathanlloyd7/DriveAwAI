# RPI_RCCAR
Final Year Project

This is my dissertation project to create a rc car and develop it to have some level of automation using images. This will be used as a log/update for myself.

03.09.19
[Added in after the fact]
Assembled electronics and did some research into the cassis of the Pi car, looked into accelerators for increased calculation speed. Built some basic functions to do directions etc. Soldered wires to motors.

08.09.19
Building on previous basic motor control I've been working on some basic GUI's using tkinter. I've created three column panels: speed, directiom, video view. The latter of which is just a default panel seen on a tutorial, currently they do not interact with the motors as I ran out of time and couldn't upgrade to an RCCar Class. Future updates will include this, at the moment the buttons will just print their expected future feature. This is a very simple draft of the panels, more items may be added in future.
In the meantime of creating the gui and learning some basic tkinter I have started the fast.ai course which library sits on top of pytorch, this looks like a very efficient way of implementing ML. And with a coral TPU accelerator I think the overall goal will be very achievable.

12.09.19
Been busy over the last few days, not much programming or research taken place. I have put a few minutes in here and there to fix problems I was stuck on last week. I can now call methods when clicking a button which is the first GUI interaction I've achieved between motor and gui. I've also been pseduo coding a rc car class, and have put together a simple set motor implementation and it works fine, will just need to fit it with actual code and test it over the gui over the coming days. Done a little quote hunting collection and put them together for my lit review too. 
--Ext: After spending time of making a functional RC class, I've hit the problem I thought I may have by putting my speed and distance into seperate containers. when speed is updated, the direction panel has no idea. For this to be solved, do I simply need to use global variables or should I make new methods that send this info over?
