import cv2
import numpy as np
import os

import random

class Control2:
    def Control2():
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

        TiempoBrillo=150
        #Colocar cubo en mapa
        cv2.rectangle(img, pt1=(x, y), pt2=(x+10, y+10), color=colorcubo, thickness=-1)

        pintar=False
        minar=False
        borrar=False
        i=0
        prendido=True
        #Zona de juego 
        while True:
            if pintar == True or minar== True or borrar== True:
                #print(i)
                if i<TiempoBrillo and prendido==True:
                    if pintar==True:
                        cv2.putText(img,text="Pintar",org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
                    if minar==True:
                        cv2.putText(img,text="Minar",org=(550,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
                    if borrar==True:
                        cv2.putText(img,text="Borrar",org=(490,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
                    i+=1
                else:
                    prendido=False
                    if pintar==True:
                        cv2.putText(img,text="Pintar",org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
                    if minar==True:
                        cv2.putText(img,text="Minar",org=(550,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
                    if borrar==True:
                        cv2.putText(img,text="Borrar",org=(490,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
                    i-=1
                    if i==0:
                        prendido=True
            else:
                i=0
                prendido=True
            if pintar==False: 
                cv2.putText(img,text="Pintar",org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
                
            if borrar == False:
                cv2.putText(img,text="Borrar",org=(490,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
                    
            if minar == False:
                cv2.putText(img,text="Minar",org=(550,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=0)
            
            #Mostrar cambios
            cv2.imshow('Escenario', img)
            #Esperar tecla
            key = cv2.waitKey(1)
            #print(key)
            #print (key) #Imprimir numero ASCII de tecla presionada
            
            # 27 es el código ASCII de la tecla esc, -1 presionar x en el boton cerrar pantalla
            if key == 27 :
                break
            if cv2.getWindowProperty('Escenario', cv2.WND_PROP_VISIBLE) < 1:
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
                    #Si minar esta activado y el color de la posicion actual es negro entonces pintar coordenada pasada de blanco
                    if minar == True and colorpasado==0:
                        cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas + 10, ypas + 10), color=255, thickness=-1)
                        
                    else:
                        #Si borrar esta activado pintar posicion pasada de blanco
                        if borrar==True:
                            cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10 , ypas+10), color=255, thickness=-1)

                        else:
                            #Si no pintar posicion pasada del color que era 
                            cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10 , ypas+10), color=colorpasado, thickness=-1)
                        
                    colorpasado=int(img[y+5,x+5])
                    #Si pintar esta activado pintar posicion pasada de algun color 
                    if pintar==True:
                        cv2.rectangle(img, pt1=(xpas, ypas), pt2=(xpas+10, ypas+10), color=colorpintar, thickness=-1)

                    #Pintar el cuadrado en la posicion nueva
                    cv2.rectangle(img, pt1=(x, y), pt2=(x + 10, y + 10), color=colorcubo, thickness=-1)
                    #Guardar posicion pasada
                    #print(colorcubo)
                    xpas=x
                    ypas=y
        cv2.destroyAllWindows()
