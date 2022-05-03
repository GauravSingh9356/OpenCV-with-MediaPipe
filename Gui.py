# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 12:17:22 2022

@author: gs935
"""


# -*- coding: utf-8 -*-



from tkinter import *
from PIL import Image, ImageTk
import os
from testPose import initializePose
from testhand import initializeHand
from faceDetector import initializeFace
from GymTrainerAI import GymTraining

def faceDetector():
   initializeFace()
   
   
def PoseDetector():
   initializePose()

def HandDetector():
   initializeHand()


def GymTrainer():
    GymTraining()
   

root = Tk()
root.title("Real Time Hand, Pose, Face Detection & AI Gym Trainer")
root.configure(bg="black")
root.geometry("700x700")


img = Image.open("image.png")

img = img.resize((700, 350), Image.ANTIALIAS)
test = ImageTk.PhotoImage(img)


label = Label( image=test)
label.pack()

b1 =Button(root, text="Face Detection",height=3,bg="#16FF01", relief="sunken", bd="3", command=faceDetector)
b1.pack(pady=15)


b2 =Button(root, text="Pose Detection",height=3,bg="#16FF01", relief="sunken", bd="3", command=PoseDetector)
b2.pack(pady=15)

b3 =Button(root, text="Hand Detection",height=3, bg="#16FF01",relief="sunken", bd="3", command=HandDetector)
b3.pack(pady=15)

b4 =Button(root, text="Gym Trainer AI",height=3, bg="#16FF01",relief="sunken", bd="3", command=GymTrainer)
b4.pack(pady=15)





















root.mainloop()


