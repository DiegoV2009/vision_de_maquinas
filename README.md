# Trabajo de visión de maquinas
En este trabajo se trabajo con opencv y python, las carpetas que se encuentran son:
* [umbralizacion][umbralizacion]: El código realiza una umbralización simple.
* [medicion del tamaño del objeto][medicion]: El código realiza calcula las áreas de los objetos de la imagen.
* [deteccion de color][deteccion]: En esta carpeta hay 2 códigos, uno se encarga de la detección del color rojo y el otro del color azúl.
* [cambio de color][cambio de color]: El código se encarga de cambiar los objetos de color rojo por objetos de color negro.
* [detección de movimiento][movimiento]:  El código toma una foto del fondo cada cierto y tiempo y compara los siguientes frames del video con esa imagen, de ese modo si hay diferencia es porque algo cambio en la escena,por ende hay movimiento:

[![deteccion-mov-1.png](https://i.postimg.cc/GmsXyV7Q/deteccion-mov-1.png)](https://postimg.cc/Xr4KMH0G)
[![deteccion-mov-2.png](https://i.postimg.cc/dDcLS7FD/deteccion-mov-2.png)](https://postimg.cc/CnJhRxzV)

* [contador de monedas][contador]: Este código suma el valor de las monedas que pasan en el video, es una simulación de una banda transportadora.
[![moneda-blanco-negro.png](https://i.postimg.cc/ZK9t5TNs/moneda-blanco-negro.png)](https://postimg.cc/ppt10MqK)
[![moneda-color.png](https://i.postimg.cc/ydft758z/moneda-color.png)](https://postimg.cc/1nqJHvFW)

* [harcascade][harcascade]: Este código reconoce objetos con ayuda de una red neuronal previamente entrenada, requiere del uso de la herramienta [cascade trainer gui][cascade trainer gui] la cual nos ayudará a entrenar una red neuronal y si se quiere de ip webcam una aplicación que se encuentra en la play store.

En la carpeta hay dos códgios, con el captura_cel se capturan las imagenes que se usaran para entrenar la red neuronal en harcascade en la carpera p las positivas que muestran el objeto y n las negativas que no muestran el objeto, el otro codigo recibe la red entrenada y detecta si está el objeto a encontrar.

[![manzana.png](https://i.postimg.cc/JzxjGWZv/manzana.png)](https://postimg.cc/Jsys2vT5)

[umbralizacion]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/umbralizacion "umbralización"
[medicion]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/medicion%20del%20tamanio%20de%20objeto "Medicion del tamaño del objeto"
[deteccion]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/Deteccion%20de%20colores "Detección de colores"
[cambio de color]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/cambio%20de%20color "cambio de color"
[movimiento]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/deteccion%20de%20movimiento "Detección de movimiento"
[contador]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/Contador_de_monedas "Contador de monedas"
[harcascade]: https://github.com/DiegoV2009/vision_de_maquinas/tree/main/harcascade_2 "harcascade"
[cascade trainer gui]: https://amin-ahmadi.com/cascade-trainer-gui/ "cascade trainer gui" 
