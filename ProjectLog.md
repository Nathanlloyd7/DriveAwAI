# DriveAwAI
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

04.10.19
Only small change today, got the save and load features working for the radio buttons on motor settings. Not as clean as I would like but it gets the job done. Next stage will be getting the loaded variables for the menu to actually interact with the panels

13.10.19
Videopanel added in, opencv needed for videostream as there is some complications when threading rpicam. Had a majority of the code done a few days ago but got stuck due to unfamiliarity with open cv syntax. Tried to use params where they weren't needed, but it is fixed now and working. Might look to add a menu that changes view by an open cv filter. "Night vision" Etc. Also looking to add "security features" where I can make use of the touch sensors on the explorer hat and make a password system.

16.10.19
Ran images for buttons through PhotoImage and they were too big and so couldn't resize, now using PIL library to edit them in app. Using images for buttons has slowed the start up slightly. Optimising this would be ideal. Changed the layout of code for rc and menu, initialising them both as self will allow me to use more features and have cleaner code.
----- I am definately keen on this password idea as well as some fun features like a horn.

21.10.19
Gone home for the week and so I haven't done any coding or research as I want some downtime, I have started to fill in a project contract however and decided to go from a scientific title to a more commerical one. I have decided to give the project an official name of 'Drive AwAI' which stands for "Drive Assisted with AI", I really like the title name and have enjoyed the downtime. I am looking forward to carrying on with the work at the end of this week. Hopefully I can add in a few fun features, the University has purchased a coral TPU on my behalf which is great. As I am already ahead of schedule, getting this device puts me even further ahead as it is the device I had in mind at the start of the project and now I do not need to replan or pay extra money to ensure I get it operational.

26.10.19
Quick little security password for my RC, thought I might as well use the touch sensors on the explorerhat as they make a great PIN entry system. Found a majority of this programming online but added the ability to change the password, next step will be saving and loading a password in. Might add it into my settings folder but I'm not sure how without deleting other settings. Works fine, just need to clean up the looping system and find out how to attach to the rest of the app, it is low priority at the moment though. Got the Coral TPU this week too, so I can start earlier than planned on ML.

10.11.19
With other deadlines looming way before this one, and already being a decent way through the development of the front end of this app I've taken my foot off the gas and will continue to do so for another week I expect. I have been making a list and updating my development timeline accordingly though. I did get a bit bored though and wanted to get the password system in place, I've made the password load in from a txt file called, passSeting.txt, and then split the string and cast so they can be formatted into a list. This means I can simply enter a string when I edit the change password setting and not have any complicated stuff. I did try and get the TPU on, but as I already had a previous install of tf and a workaround method for 3.5 python. It would seem as they now support 3.7 there is a clash, will have to uninstall libraries or reformat the SD and reinstall from scratch.

15.02.20
Long time since the last log, bogged down with other uni work but I have been working on this as some commits show. I have a model working with the TPU but it currently doesn't effect the Pi, it can see but not act upon anything. I have also been working on the chassis and its nearly complete. Because of this I can add directional functionality... however, it may need fine tuning. I have spent some of the day just cleaning up the files, I want be able to curl in my files between different SD cards and have everything pre-installed by doing so. So a bit of housekeeping is going to occur to do this.

17.02.20
Have created requirements file.
Have also added extra security by hashing the pin passwords.**Hash of these commits matches 4321, however, github adds whitespace at the end of the line, so please remove this**

03.03.20
Removed flip from the video stream. 
Spent the last week finishing up the core driving elements, motors are now installed using 3D printed elements, car can now be driven using GUI. Need to shift the minimum speed selectable though in slider. 35 is too slow. 50 is new minimum.

Also bought toy model traffic signs, taken 120 photos containing around 250 object instances. Used LabelImg to box the signs and toy person. Got a few left to do as I need to retake a few photos due to poor image quality. After this I can xml -> CSV -> TFRecord ... and then start training (transfer learning on MobileNet v2 SSD COCO), COCO contains a few objects that I could use anyway, such as cars, people, trucks et. MobileNet v2 SSD is well documented and middleground of accuracy and speed. May try and train my own from scratch not using COCO but will see.
