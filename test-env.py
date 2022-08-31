# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 12:25:24 2021

@author: ENGINEER
"""
# Import tje libararies
import cv2
import dlib
import face_recognition


# Printing the versions
print(cv2.__version__)
print(dlib.__version__)
print(face_recognition.__version__)


# Loading the image to detect
image_test = cv2.imread('Images/testing/kashif.png')

# Showing the current image with title
cv2.imshow("Image", image_test) 
