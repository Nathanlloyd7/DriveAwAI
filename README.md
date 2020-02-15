# DriveAwAI - Final Year Project - Nathan Lloyd
Welcome to my Final Year Project as an undergraduate, the aim of this project is to have a semi autonomous vehicle that naturally has the ability to toggle between assisted. This will be done utilising a Pi 4, Coral TPU and explorerHAT Pro.

## Shopping List

Item | COST | Link
-----|------|-----
Raspberry Pi 4 | £30 - 50 | https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052740158
SD Card (Recommend 32GG+) | ?? | UP2U
ExplorerHat Pro | £20 | https://thepihut.com/products/explorer-hat
Coral TPU | £75| https://www.mouser.co.uk/ProductDetail/Coral/G950-01456-01?qs=u16ybLDytRbcxxqFKdbhgQ%3D%3D&vip=1&gclid=Cj0KCQiAyp7yBRCwARIsABfQsnTXXBOMc39uSGN2DqE6U5CDuxEE6uXcuEYrENukWt5UyDaJZwTOfbQaAoTaEALw_wcB
PiCam V2 | £25 | https://thepihut.com/products/raspberry-pi-camera-module
PiCam Mount | £3 | https://shop.pimoroni.com/products/raspberry-pi-camera-mount
Motors & Wheels | £8 | 2 PCS DC Gear Motor + Tire Wheel for Arduino DC 3V-6V
Fan Shim | £10 | https://thepihut.com/products/fan-shim-for-raspberry-pi
Ninja Case | £8.50 | https://thepihut.com/products/pibow-4-coupe-case-for-raspberry-pi-4b?variant=20452597661758  
Dragging Wheel (Shooping Cart) | £3 | https://www.amazon.co.uk/gp/product/B007OXBMQM/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1
Jumper Wires M-M | £5 | https://www.amazon.co.uk/gp/product/B0144HG2RE/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
LED's x2 | £2.50 | https://thepihut.com/products/adafruit-diffused-5mm-led-pack-5-leds-each-in-5-colors-25-pack-ada4203
Resistor x2 | £6 | https://thepihut.com/products/ultimate-resistor-kit
Blue Tape | £1 | https://www.amazon.co.uk/gp/product/B0001IXA76/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1
Pi Cam Ribbon Ext | £4 | https://www.amazon.co.uk/gp/product/B01MU2HAOM/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1
Battery Pack | TBD | TBD
Total| £200 -£250 | I've not gone out to look for the best deal, so please do that yourself.

Some of the above aren't exactly what I bought and in some cases I had parts laying around from previous projects. This is just a guide to what you may need if you fully recreate. 

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
Step 1: 
>Enable i2c, SSH, Camera and VNC  in Raspberry Pi config.
Step 2:
>Download the project if you haven't already.
Step 3:
>Unzip
Step 4:
>Navigate to the directory (/DriveAwAI-Nathanlloyd7) through terminal, here you can find the requirements doc. Then Run 
>pip install --user --requirement Requirements.txt
