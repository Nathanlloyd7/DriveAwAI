# DriveAwAI - Final Year Project - Nathan Lloyd
Welcome to my Final Year Project as an undergraduate, the aim of this project is to have a semi autonomous vehicle that naturally has the ability to toggle between assisted. This will be done utilising a Pi 4, Coral TPU and explorerHAT.

## Shopping List

Item | COST | Link
-----|------|-----
Raspberry Pi 4 | £40 | ??
ExplorerHat | £75 | https://www.mouser.co.uk/ProductDetail/Coral/G950-01456-01?qs=u16ybLDytRbcxxqFKdbhgQ%3D%3D&vip=1&gclid=Cj0KCQiAyp7yBRCwARIsABfQsnTXXBOMc39uSGN2DqE6U5CDuxEE6uXcuEYrENukWt5UyDaJZwTOfbQaAoTaEALw_wcB
Coral TPU | ??|??
PiCam V2 | ??|??
Motors | ??|??
Wheels |?? |??
Fan Shim | ?? | ??
Dragging Wheel (Shooping Cart) |?? |??
Jumper Wires M-M |?? |??
LED's x2 |??|??
Resistor x2 | ??|??

## Car Body
I have had a lot of help from a friend designing a chassis to fit the items I've accumilated, you can use whatever you want for your body... but the CAD models and designs will be displayed within a folder shortly.


## Installing Coral TPU
Step 1: Install Coral TPU - https://coral.ai/docs/accelerator/get-started/

>echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
>curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
>sudo apt-get update

>sudo apt-get install libedgetpu1-std

Step 2: Install TF for Python - https://www.tensorflow.org/lite/guide/python
>pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl

Step 3: Check Installs by running a model
>mkdir coral && cd coral
>git clone https://github.com/google-coral/tflite.git

>cd tflite/python/examples/classification
>bash install_requirements.sh

>python3 classify_image.py \
>--model models/mobilenet_v2_1.0_224_inat_bird_quant_edgetpu.tflite \
>--labels models/inat_bird_labels.txt \
>--input images/parrot.jpg

# Installing Requirements
First you need to enable i2c, SSH, Camera and VNC  in Raspberry Pi config.

Navigate to the directory (/DriveAwAI-Nathanlloyd7) here you can find the requirements doc. Then Run ->
>pip install --user --requirement Requirements.txt
