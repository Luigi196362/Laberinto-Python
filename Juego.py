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
    posicion_inicialX=random.randrange(0,571,30)
    posicion_inicialY=random.randrange(0,571,30)
    if img[posicion_inicialY,posicion_inicialX] > 0 and img[posicion_inicialY+10,posicion_inicialX+10] > 0:#and img[posicion_inicial+10,posicion_inicial+10]>0:
        break
    
    
    
zona=1
#Posiocion x y 
x = posicion_inicialX
y = posicion_inicialY
#Posicion x y pasada
xpas = x
ypas = y
#Velocidad
v = 10
colorcubo=155
#Color de pintura
colorpintar=100
colorpasado=int(img[y+5,x+5])
#Colocar cubo en mapa
cv2.rectangle(img, pt1=(x, y), pt2=(x+10, y+10), color=colorcubo, thickness=-1)

pintar=False
minar=False
borrar=False

#Zona de juego 
while True:
    if pintar == True:
        cv2.putText(img,text="Pintar",org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=255,thickness=-1)
    else: 
        cv2.putText(img,text="Pintar",org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=0,thickness=-1)
        
    if borrar == True:
        cv2.putText(img,text="Borrar",org=(490,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=255,thickness=-1)
    else: 
        cv2.putText(img,text="Borrar",org=(490,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=0,thickness=-1)
            
    if minar == True:
        cv2.putText(img,text="Minar",org=(550,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=255,thickness=-1)
    else: 
        cv2.putText(img,text="Minar",org=(550,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
        #cv2.rectangle(img,pt1=(580,615),pt2=(590,625),color=0,thickness=-1)

    
    #Mostrar cambios
    cv2.imshow('Escenario', img)
    #Esperar tecla
    key = cv2.waitKey(0)
    #print (key) #Imprimir numero ASCII de tecla presionada
    
    # 27 es el código ASCII de la tecla esc, -1 presionar x en el boton cerrar pantalla
    if key == 27 or key ==-1:
        break
    
    #Activar minar con tecla E
    if key == 108:
        if minar == True:
            minar = False
        else: 
            minar=True
            
    #Activar pintar con tecla  Q 
    if key == 106:
        if pintar == True:
            pintar = False
        else: 
            pintar=True
            borrar=False

    #Borrar 
    if key == 107:
        if borrar == True:
            borrar = False
        else: 
            borrar=True
            pintar=False        
    #Reiniciar mapa
    if key == 114:
        img = cv2.imread('Escenarios/Escenario 1.jpg', cv2.IMREAD_GRAYSCALE)
        cv2.rectangle(img, pt1=(x, y), pt2=(x + 10, y + 10), color=colorcubo, thickness=-1)
              
    #Si presiona WASD entonces...
    if key == 119 or key == 97 or key == 115 or key == 100:  
        #Si minar esta activado desactivar comprobaciones     
        if minar == True:
                #Arriba
                if (key==119):
                    y-=v
                #Izquierda
                if (key==97):
                    x-=v
                #Abajo
                if (key==115):
                    y+=v
                #Derecha
                if (key==100):
                    x+=v
                    
        #Si minar esta desactivado activar comprobaciones
        else:
                # arriba
                if (key == 119) and (img[y - v, x] > 0) and (img[y - v, x+10] > 0):
                    
                    if (y - 1 < 0):
                        img = cv2.imread('Escenarios/Escenario 2.jpg', cv2.IMREAD_GRAYSCALE)
                        y=590
                    else:
                        y -= v
                # izquierda
                if (key == 97) and (x - v >= 0) and (img[y , x - v] > 0) and (img[y+10 , x - v] > 0):
                    x -= v
                
                # abajo
                if (key == 115) and (y + (v+10) < img.shape[0]) and (img[y + (v+10), x] > 0) and (img[y + (v+10), x+10] > 0):
                    #print(x,y)
                    y += v
                    
                # derecha
                if (key == 100) and (x + (v+10) < img.shape[1]) and (img[y, x + (v+10)] > 0) and (img[y+10, x + (v+10)] > 0):
                    x += v
        #Si hubo movimiento (comprueba si la posicion anterior y la  posicion nueva es distinta)
        if (xpas!=x or ypas !=y):
            
            #Si pintar esta activado pintar la posicion pasada de color gris
            #if (pintar == True or borrar==True ):

            #Si pintar esta desctivado pintar posicion pasada para pintar de blanco la zona pasada "Borrar"
            #else:
            #print ("color " ,colorpasado)
            if minar == True and colorpasado==0:
                cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas + 10, ypas + 10), color=255, thickness=-1)
            else:
                if borrar==True:
                    cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10 , ypas+10), color=255, thickness=-1)
                else:
                    cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10 , ypas+10), color=colorpasado, thickness=-1)
                
            colorpasado=int(img[y+5,x+5])

            if pintar==True:
                cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10, ypas+10), color=colorpintar, thickness=-1)

            #Pintar el cuadrado en la posicion nueva
            cv2.rectangle(img, pt1=(x, y), pt2=(x + 10, y + 10), color=colorcubo, thickness=-1)
            #Guardar posicion pasada
            #print(colorcubo)
            xpas=x
            ypas=y
cv2.destroyAllWindows()
