import cv2
import numpy as np
import os
from Funciones.Generador import GenerarEscenario 
from Funciones.Eliminar import ElimiarEscenarios

#Eliminar escenarios pasados
ElimiarEscenarios.Eliminar()

#Limpiar consola
os.system("cls")

#Generar escenarios
GenerarEscenario.GenerarImagenes()

#Crear mapa
imagen1=cv2.imread('Escenarios/Escenario 1.jpg')
imagen2=cv2.imread('Escenarios/Escenario 2.jpg')
concat_horizontal = cv2.hconcat([imagen1, imagen2])
#resized_image = cv2.resize(concat_horizontal, (600, 600))
resized_image = cv2.resize(concat_horizontal, (0,0), fx=0.4, fy=0.4) 
cv2.imshow('concat_horizontal', concat_horizontal)
cv2.imshow('concat_horizontal', resized_image)
 

img = cv2.imread('Imagenes/Proyecto.jpg') # Leer la imagen
cv2.imshow('Proyecto', img) # Mostrar la imagen en una ventana llamada Proyecto
cv2.waitKey(0)
cv2.destroyWindow('Proyecto')
img = cv2.imread('Escenarios/Escenario 1.jpg') # Leer la imagen
while True:
    cv2.imshow('Escenario', img)
    key = cv2.waitKey(0)
    if key == 27: # 27 es el código ASCII de la tecla esc
        break
    
        