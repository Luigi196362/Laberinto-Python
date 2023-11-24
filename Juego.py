import cv2
import numpy as np
import os
from Funciones.Generador import GenerarEscenario 
from Funciones.Eliminar import ElimiarEscenarios
import random

#Eliminar escenarios pasados
ElimiarEscenarios.Eliminar()

#Limpiar consola
os.system("cls")

#Generar escenarios
GenerarEscenario.GenerarImagenes()



img = cv2.imread('Escenarios/Escenario 1.jpg', cv2.IMREAD_GRAYSCALE)  # Leer la imagen

#Crear zona de aparicion aleatoria dependiendo si es blanco o negro
while True:
    posicion_inicial=random.randrange(0,601,20)
    if img[posicion_inicial,posicion_inicial]>0:
        break
zona=1
#Posiocion x y 
x = posicion_inicial
y = posicion_inicial
#Posicion x y pasada
xpas = x
ypas = y
#Velocidad
v = 20
colorcubo=155
#Colocar cubo
cv2.rectangle(img, pt1=(x, y), pt2=(x+10, y+10), color=colorcubo, thickness=-1)

#Zona de juego
while True:
    cv2.imshow('Escenario', img)
    key = cv2.waitKey(0)

    # 27 es el código ASCII de la tecla esc
    if key == 27:
        break

    if key == 119 or key == 97 or key == 115 or key == 100:

        # arriba
        if (key == 119)  and (img[y - 1, x+5] > 0):
            
            if (y - 1 < 0):
                img = cv2.imread('Escenarios/Escenario 2.jpg', cv2.IMREAD_GRAYSCALE)
                y=590
            else:
                y -= v
        # izquierda
        if (key == 97) and (x - v >= 0) and (img[y + 5 , x - v] > 0):
            x -= v
          
        # abajo
        if (key == 115) and (y + 11 < img.shape[0]) and (img[y + 12, x + 4] > 0):
            print(x,y)
            y += v
               
        # derecha
        if (key == 100) and (x + 11 < img.shape[1]) and (img[y + 5, x + 12] > 0):
            x += v
            
    if (xpas!=x or ypas !=y):
        cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas + 10, ypas + 10), color=255, thickness=-1)
        cv2.rectangle(img, pt1=(x, y), pt2=(x + 10, y + 10), color=colorcubo, thickness=-1)
        xpas=x
        ypas=y
cv2.destroyAllWindows()
