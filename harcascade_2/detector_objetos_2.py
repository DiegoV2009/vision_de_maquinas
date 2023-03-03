import cv2
import numpy as np
import imutils
import os

cap = cv2.VideoCapture("http://192.168.0.10:8080/video")

Clasificador = cv2.CascadeClassifier('cascade.xml')

while True:
    
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    toy = Clasificador.detectMultiScale(gray,
    scaleFactor = 1.2,
    minNeighbors = 100,
    minSize=(200,200),
    maxSize=(1000,1000))

    for (x,y,w,h) in toy:
        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame,'Manzana',(x,y-10),2,0.7,(0,255,0),2,cv2.LINE_AA)

    frame = imutils.resize(frame, width=1000)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('d'):
        break
cap.release()
cv2.destroyAllWindows()