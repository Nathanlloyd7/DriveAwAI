import numpy as np
import cv2
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

#videostream RPiCam2
class RCVideoPanel:
    def __init__(self, root, frame): 
        self.root = root
        self.frame = frame
#Video Frame
        self.imageFrame = Frame(self.frame, width=600, height=500)
        self.imageFrame.grid(row=0, column=0, padx=10, pady=2)
#Capture video frames
        self.lmain = tk.Label(self.imageFrame) #attach image to label
        self.lmain.grid(row=0, column=0)
        self.capture = cv2.VideoCapture(0)
        self.show_frame()  
        
    def show_frame(self):
        _, frame = self.capture.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(10, self.show_frame) #takes a photo but doesn't fully work


