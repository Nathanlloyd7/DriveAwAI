# DriveAwAI - Final Year Project - Nathan Lloyd
Brief intro to content

## Shopping List
Raspberry Pi 4
ExplorerHat
Coral TPU
PiCam V2

Motors
Wheels
Dragging Wheel (Shooping Cart)
Jumper Wires M-M
LED's x2
Resistor x2

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
