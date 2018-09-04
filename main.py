# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 17:23:05 2018

@author: Kay
"""

import numpy as np
import cv2
import sys



if __name__ == '__main__' :
 
    # Set up tracker.
    # Instead of MIL, you can also use
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]
 
   # tracker = cv2.Tracker_create(tracker_type)
    
    if tracker_type == 'BOOSTING':
        tracker = cv2.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.TrackerTLD_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.TrackerMedianFlow_create()
    if tracker_type == 'GOTURN':
        tracker = cv2.TrackerGOTURN_create()
    if tracker_type == 'MOSSE':
        tracker = cv2.TrackerMOSSE_create()
    if tracker_type == "CSRT":
        tracker = cv2.TrackerCSRT_create()

file='C:/Users/JP/Documents/Python Scripts/Fly_tracking/1.avi'
video=cv2.VideoCapture(file)


# Check if camera opened successfully
if (video.isOpened()== False): 
  print("Error opening video stream or file")


length=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)


#to play video
while(video.isOpened()):
    ret, frame =video.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    retval, threshold = cv2.threshold(frame, 75, 255, cv2.THRESH_BINARY)
    #th = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    
    
    if ret == True:
        cv2.imshow('Frame', frame)
        cv2.imshow('Threshold', threshold)
        #cv2.imshow('Adaptive threshold', th)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
   
    else:
        break
    
    
cap.release()
cv2.destroyAllWindows()