import cv2
import numpy as np

video = cv2.VideoCapture('video_monedas_2.mp4')
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

i = 0
dinero = 0
comprobar_contacto_real=0

while True:
  ret, frame = video.read()
  
  if ret == False: 
    break
  
  area_pts = np.array([[0, 640], [frame.shape[1], 640], [frame.shape[1], 500], [0, 500]])

  # Con ayuda de una imagen auxiliar, determinamos el área
  # sobre la cual actuará el detector de movimiento
  imAux = np.zeros(shape=(frame.shape[:2]), dtype=np.uint8)
  imAux = cv2.drawContours(imAux, [area_pts], -1, (255), -1)
  image_area = cv2.bitwise_and(frame, frame, mask=imAux)    

  
  gray = cv2.cvtColor(image_area, cv2.COLOR_BGR2GRAY)
  
  

  if i%1000 == 0:
    bgGray = gray
  if i > 20:
    dif = cv2.absdiff(gray, bgGray)
    _, th = cv2.threshold(dif, 30, 255, cv2.THRESH_BINARY)
    
    fgmask = th
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    fgmask = cv2.dilate(fgmask, None, iterations=10) 
    
    cnts, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame, cnts, -1, (0,0,255),2)        
    
    moneda_detectada = False  
    for cnt in cnts:
      area = cv2.contourArea(cnt)
      if area > 4000:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,255), 1)
            
            # Si el auto ha cruzado entre 440 y 460 abierto, se incrementará
            # en 1 el contador de autos
            
            if 625 < (y+h) < 635:  
              cv2.line(frame, (0, 635), (640, 635), (0, 255, 0), 3)  
              aux = i-comprobar_contacto_real
              comprobar_contacto_real=i
              if aux>20:
                if area < 10000:
                  dinero = dinero+50
                elif area< 12000:
                  dinero = dinero+100
                elif area< 13000:
                  dinero = dinero+200
                elif area< 15000:
                  dinero = dinero+500
                elif area< 20000:
                  dinero = dinero+1000
                
              
              
    cv2.drawContours(frame, [area_pts], -1, (255, 0, 255), 2)
    cv2.line(frame, (0, 635), (640, 635), (0, 255, 255), 1)
    
    cv2.putText(frame, str(dinero), (frame.shape[1]-100, 250),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 2)

  
  cv2.imshow('Frame',frame)
 
  i = i+1
  
  if cv2.waitKey(40) & 0xFF == ord ('q'):
    break

video.release() 