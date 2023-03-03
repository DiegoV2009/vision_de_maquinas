import cv2
import numpy as np
import imutils
import os

Datos = 'n'
if not os.path.exists(Datos):
	print('Carpeta creada: ', Datos)
	os.makedirs(Datos)

cap = cv2.VideoCapture("http://192.168.0.10:8080/video")

x1, y1 =100, 80
x2, y2 = 800, 800

count = 0
while True:

	ret, frame = cap.read()
	if ret == False:  break
	imAux = frame.copy()
	cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

	objeto = imAux[y1:y2,x1:x2]
	objeto = imutils.resize(objeto, width=38)
	# print(objeto.shape)

	k = cv2.waitKey(1)
	if k == ord('c'):
		cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
		print('Imagen almacenada: ', 'objeto_{}.jpg'.format(count))
		count = count + 1
	if k == ord('d'):
		break

	frame = imutils.resize(frame, width=600)
	cv2.imshow('frame',frame)
	cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()