   #new
import cv2
import numpy as np
import dlib
import pyautogui
import time

pyautogui.FAILSAFE = False 
#global z
cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray,0)
    dimension=frame.shape
    height = frame.shape[0]
    width = frame.shape[1]
   
    cv2.line(frame,(int((width/2)+100),0),(int((width/2)+100),height),(0,255,0),2)
    cv2.line(frame,(int((width/2)-100),0),(int((width/2)-100),height),(0,255,0),2)
    cv2.line(frame,(0,int(height/2)),(width,int(height/2)),(0,255,0),2)
   
           
    for face in faces:
        #print(face)
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
        #cv2.line(frame,(200,z),(800,z),(0,0,250),5)

        landmarks = predictor(gray, face)

        #for n in range(0, 68):
        x= landmarks.part(27).x
        y = landmarks.part(27).y
        print(x,y)
        #cv2.circle(frame, (x, y), 4, (0, 0, 139), -1)
        
       # cv2.line(frame,(x,0),(y,10),(0,255,0),2)

        if(y<(int(height/2))):   
         print("up")
         pyautogui.press('up')
         pyautogui.keyUp('up')
           
        elif(x>340):
         print('Right')
         pyautogui.press('right')
         pyautogui.keyUp('right')
      
        elif(x<300 and y>160):
         print('left')
         pyautogui.press('left')
         pyautogui.keyUp('left')

        time.sleep(0.001)

     
          

       
        
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

