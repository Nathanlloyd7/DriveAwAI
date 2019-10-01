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

!!I think the best way forward would be to initialize my rc car in the RCTK window and have all my panels speak to this window.

19.09.19
Moved into Uni halls now, so potentially more frequent work. Merged the speed and direction panel into a movement panel. Adding diagonal turning too, currently the buttons don't match up in size, but eventually I will use images(arrows) to point in the direction. DIrections have not been coded in other than forward and backward as there is no chassis, so right and left is undecided. Added in a scale/slider for speed as it is more representative of real driving. Also added some basic menu buttons. Need to clean the code out and ideall would like to OOP up my menu buttons to make RCTK cleaner. But it is less important as these are secondary features. Still trying to find out how to access a stream of the picam too. Have some ideas but not seen any absolutes as of yet.

23.09.19
Added minor features to some of the menu items and changed about from a new window to a message box. I can see these menu items taking up a lot of room and it's not too clean coding having them in the RCTK file. Might need to implement OOP in the future to bring these menu items in. However I might save cleaning up my code until I have working up features as it is more important I get things working first.

27.09.19
Swapped to a pair of radio buttons for my one menu item. the menu saves and loads as expected but I can't display in the log box. I can sometimes get one working but not the other, could be an issue with the var or the r+/w+ access.

01.10.19
Created a new menu class to clean up RCTKWindow, I broke the save and load feature because of it but very happy with the cleaner approach. This approach as I followed a stack overflow posting meant I had to drop my root naming convention in RCTK in favour of initialising by tk.TK__init__(self) but other than those two issues fairly simple. Would be nice if I could get controller settings for a future update. Also realised I haven't posted the widget icon 'realcar1.png' but fairly straight forward so I wont post. Really happy with progress so far, think I'm going to go down an opencv & Tensor flow route so I can have an opencv stream in tkinter whereas currently getting the video in a frame is out of my knowledge.
