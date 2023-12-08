import cv2
import numpy as np
import os
from Funciones.Generador import GenerarEscenario 
from Funciones.Eliminar import ElimiarEscenarios
from Controles.Snake import Snake
from Controles.Control2 import Control2
import random
#from playsound import playsound

#ruta_audio = "Meme.mp3"
while True:
    Salir = True
    #Eliminar escenarios pasados
    #ElimiarEscenarios.Eliminar()

    #Limpiar consola
    os.system("cls")

    #Generar escenarios
    Cantidad=GenerarEscenario.GenerarImagenes()
                            # Ruta del archivo de audio
    os.system("cls")
    TipoControl=int(input("Tipo de control: \n1.-Cubito \n2.-Snake "))
    
    if TipoControl==1:
        Control2.Control2()
    else:    
        Snake.Snake()
    os.system("cls")
    
    
    img = cv2.imread('Imagenes/GameOver.jpg', cv2.IMREAD_GRAYSCALE)
    #img = cv2.imread('Imagenes/Hormiga.jpg', cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Escenario', img)
    key = cv2.waitKey(1)
    #playsound(ruta_audio)
    while True:
                    
        key = cv2.waitKey()
        if key == 114:
            Salir=False
            cv2.destroyAllWindows()
            break
        if key == 27 :
            break
        if cv2.getWindowProperty('Escenario', cv2.WND_PROP_VISIBLE) < 1:
            break
    
    if Salir==True:
        break         
