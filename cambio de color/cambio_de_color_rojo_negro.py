import cv2
import numpy as np
import imutils


cap = cv2.VideoCapture(0)
rojoBajo1 = np.array([0, 140, 90], np.uint8)
rojoAlto1 = np.array([8, 255, 255], np.uint8)
rojoBajo2 = np.array([160, 140, 90], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

azulb = np.array([254,0,0], np.uint8)
azula = np.array([255,0,0], np.uint8)
while True:
  ret,frame = cap.read()
  frame = imutils.resize(frame, width=500)
 
  if ret==True:
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    maskRojo1 = cv2.inRange(frameHSV, rojoBajo1, rojoAlto1)
    maskRojo2 = cv2.inRange(frameHSV, rojoBajo2, rojoAlto2)
    maskAzul2 = cv2.inRange(frame, azulb, azula)
    mask = cv2.add(maskRojo1,maskRojo2)
    mask_color = cv2.bitwise_and(frame, frame, mask= mask)
    
    ret,bina = cv2.threshold( mask_color,10,255, cv2.THRESH_BINARY)
    mask_color_not = cv2.bitwise_not(mask_color)      
    #cv2.imshow('Cambio_color', azul)
    cv2.imshow('maskAzul', mask_color_not)
    #cv2.imshow('maskAzulvis', maskAzulvisnot)
    imagen_cambio_color = cv2.bitwise_and(frame, mask_color_not) 
    #esta = cv2.add(frame, maskrojanot)
    cv2.imshow('mask',  imagen_cambio_color)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break
cap.release()
cv2.destroyAllWindows()