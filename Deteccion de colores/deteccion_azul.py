import cv2
import numpy as np

cap = cv2.VideoCapture(0)
azulBajo = np.array([90, 50, 0], np.uint8)
azulAlto = np.array([130, 255, 255], np.uint8)

while True:
  ret,frame = cap.read()
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    maskAzul = cv2.inRange(frameHSV, azulBajo, azulAlto)
   
    maskAzulvis = cv2.bitwise_and(frame, frame, mask= maskAzul)        
    cv2.imshow('frame', frame)
    cv2.imshow('maskAzul', maskAzul)
    cv2.imshow('maskAzulvis', maskAzulvis)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()