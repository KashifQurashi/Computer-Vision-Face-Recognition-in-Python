# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:45:04 2021

@author: ENGINEER
"""

#Importing the required libraries

import cv2
import  face_recognition

#Loading the image to detect 
image_to_detect = cv2.imread('images/trumjpgp-modi.')

#Detect all faces in the image
#arguments are image,no_of_times_to_upsample, model
all_face_locations = face_recognition.face_locations(image_to_detect,model='hog')

#Print the number of faces detected
print('There are {} no of faces in this image'.format(len(all_face_locations)))

# Looping through the face locations
for index,current_face_location in enumerate(all_face_locations):
    #spliting the tuple to get the four position values of current face 
    top_pos,right_pos,bottom_pos,left_pos = current_face_location
    #printing the location of current face
    print('Found face {} at top:{},right:{},bottom:{},left:{}'.format(index+1,top_pos,right_pos,bottom_pos,left_pos))
    #slicing the current face from main image 
    current_face_image = image_to_detect[top_pos:bottom_pos,left_pos:right_pos]
    #showing the current face with dynamic title
    cv2.imshow("Face no "+str(index+1),current_face_image)