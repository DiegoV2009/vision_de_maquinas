import cv2
import numpy as np

imagen = cv2.imread('cartas.jpg')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
grises = cv2.bitwise_not(grises)
bordes = cv2.Canny(grises, 1, 150)
areas_img = 255*np.ones((600,200,3),dtype=np.uint8)

ctns, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
i=0
for c in ctns:
  i=i+1
  area = cv2.contourArea(c)
  area_txt ='area '+str(i)+': '+ str(area)

  cv2.putText(areas_img, area_txt, (10+i,30*i), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
  (0, 0, 0), 1)

cv2.drawContours(imagen, ctns, -1, (0,0,255), 2)
print('Número de contornos encontrados: ', len(ctns))
texto = 'Contornos encontrados: '+ str(len(ctns))

cv2.imshow('Areas', areas_img)
cv2.imshow('Imagen', grises)
cv2.imshow('Imagen', imagen)

cv2.waitKey(0)
cv2.destroyAllWindows()