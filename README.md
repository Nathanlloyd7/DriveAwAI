# DriveAwAI
Final Year Project


Step 1: Install Coral TPU - https://coral.ai/docs/accelerator/get-started/

>echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
>curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
>sudo apt-get update

>sudo apt-get install libedgetpu1-std

Step 2: Install TF for Python - https://www.tensorflow.org/lite/guide/python
>pip3 install https://dl.google.com/coral/python/tflite_runtime-2.1.0.post1-cp37-cp37m-linux_armv7l.whl
