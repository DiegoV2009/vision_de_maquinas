import cv2

imagen = cv2.imread('monedas.jpg')
grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
_,th = cv2.threshold(grises, 220, 255, cv2.THRESH_BINARY_INV)

contornos,hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (255,0,0), 2)
print('Contronos: ', len(contornos))

cv2.imshow('Imagen', imagen)
cv2.imshow('Imagen2', th)
cv2.waitKey(0)
cv2.destroyAllWindows()