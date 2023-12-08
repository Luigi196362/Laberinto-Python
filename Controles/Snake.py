import cv2
import numpy as np
import os
#from Funciones.Generador import GenerarEscenario 
#from Funciones.Eliminar import ElimiarEscenarios
import random
#from playsound import playsound

class Snake:
    
    def Snake():
        
        
        #ruta_audio = "Meme.mp3"
        Mapa = [[0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],
                [0,0,0,0,0],]
        #Y,X
        Mapa[2][2]=1
        Mapa[1][2]=2
        Mapa[3][2]=3
        Mapa[2][3]=4
        Mapa[2][1]=5
        MapaX=2
        MapaY=2

        for fila in Mapa:
            print(fila)
        #input()


        img = cv2.imread('Escenarios/Escenario 1.jpg', cv2.IMREAD_GRAYSCALE)  # Leer la imagen

        #Crear zona de aparicion aleatoria dependiendo si es blanco o negro
        while True:
            posicion_inicialX=random.randrange(0,571,20)
            posicion_inicialY=random.randrange(0,571,20)
            if img[posicion_inicialY,posicion_inicialX] > 0 and img[posicion_inicialY+10,posicion_inicialX+10] > 0:#and img[posicion_inicial+10,posicion_inicial+10]>0:
                break
        zona=1
        #Posiocion x y 
        x = posicion_inicialX
        y = posicion_inicialY
        v = 20
        colorcubo=150
        Perdio=False
        #Posicion x y pasada
        xpas = []
        ypas = []

        for i in range(2):
            xpas.append(x)
            ypas.append(y)

        c=1
        c2=0
        direccion=0
        cv2.rectangle(img, pt1=(x, y), pt2=(x+19, y+19), color=colorcubo, thickness=-1)
        cv2.rectangle(img, pt1=(x, y), pt2=(x+19, y+19), color=colorcubo-20, thickness=0)

        while True:

            cv2.rectangle(img,pt1=(430,601),pt2=(640,640),color=50,thickness=-1)
            cv2.putText(img,text="Puntos: {:.0f}".format(c-1),org=(430,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=250)
            cv2.imshow('Escenario', img)
            #Esperar tecla
            key = cv2.waitKey(300)

            if key == 27 :
                break
            if cv2.getWindowProperty('Escenario', cv2.WND_PROP_VISIBLE) < 1:
                break
            
            #Arriba
            if (key==119):
                if direccion!=3:
                    direccion=1
            #Izquierda
            if (key==97):
                if direccion!=4:
                    direccion=2
            #Abajo
            if (key==115):
                if direccion !=1: 
                    direccion=3
            #Derecha
            if (key==100):
                if direccion!=2:
                    direccion=4
                    
            if (key==32):
                direccion=0
            #Arriba
            if(direccion==1) :  
                y -= v
            #Izquierda
            if(direccion==2):
                x-=v  
            #Abajo  
            if(direccion==3):    
                y+=v
            #Derecha
            if(direccion==4):    
                x+=v
                
            if (y<0 or y>=600) or (x<0 or x>=600):
                for i in range (len(xpas)):
                    #print(i)
                    cv2.rectangle(img, pt1=(xpas[i], ypas[i]), pt2=(xpas[i]+19 , ypas[i]+19), color=255, thickness=-1)
                cv2.imwrite('Escenarios/Escenario '+str(Mapa[MapaY][MapaX])+'.jpg', img)
                #Abajo
                if (y>=600):
                    #print("borde")
                    #print(Mapa[MapaY+1][MapaX])
                    if Mapa[MapaY+1][MapaX] > 0 and MapaY >=0:
                        MapaY+=1
                        img = cv2.imread('Escenarios/Escenario '+str(Mapa[MapaY][MapaX])+'.jpg', cv2.IMREAD_GRAYSCALE)
                    y=0
                    
                #Arriba
                if (y<0):
                    #print("borde")
                    #print(Mapa[MapaY+1][MapaX])
                    if Mapa[MapaY-1][MapaX] > 0 and MapaY >=0:
                        MapaY-=1
                        img = cv2.imread('Escenarios/Escenario '+str(Mapa[MapaY][MapaX])+'.jpg', cv2.IMREAD_GRAYSCALE)
                    y=580
                    
                #Derecha
                if (x>=600):
                    #print("borde")
                    #print(Mapa[MapaY+1][MapaX])
                    if Mapa[MapaY][MapaX+1] > 0 and MapaY >=0:
                        MapaX+=1
                        img = cv2.imread('Escenarios/Escenario '+str(Mapa[MapaY][MapaX])+'.jpg', cv2.IMREAD_GRAYSCALE)
                    x=0
                    
                #Izquierda   
                if (x<0):
                    #print("borde")
                    #print(Mapa[MapaY+1][MapaX])
                    if Mapa[MapaY][MapaX-1] > 0 and MapaY >=0:
                        MapaX-=1
                        img = cv2.imread('Escenarios/Escenario '+str(Mapa[MapaY][MapaX])+'.jpg', cv2.IMREAD_GRAYSCALE)
                    x=580
                #print (x,y)
                #print(xpas[0],ypas[0])
                    

                for i in range (len(xpas)):
                    xpas.insert(0,-20)
                    ypas.insert(0,-20)
                    xpas.pop()
                    ypas.pop()
                #print(xpas)
                #print(ypas)
            else:
                if img[y,x]<150 and direccion !=0:
                    x=xpas[0]
                    y=ypas[0]
                    Perdio=True
                    break
                    

            if (xpas[0]!=x) or (ypas[0]!=y):
                #print (img[y+10,x+10])
                if img[y+10,x+10]==200 or 90<img[y+10,x+10]<160:
                    if img[y+10,x+10]==200:
                        c+=1
                    if 90<img[y+10,x+10]<160:
                        c2+=5
                            
                else:
                    if c2==0:
                        xpas.pop()
                        ypas.pop()
                    else:
                        c2-=1
                        c+=1

                xpas.insert(0,x)
                ypas.insert(0,y)
                cv2.rectangle(img, pt1=(xpas[c], ypas[c]), pt2=(xpas[c]+19 , ypas[c]+19), color=255, thickness=-1)
                cv2.rectangle(img, pt1=(x, y), pt2=(x + 19, y + 19), color=colorcubo, thickness=-1)
                cv2.rectangle(img, pt1=(x, y), pt2=(x+19, y+19), color=colorcubo-20, thickness=0)
                    
            if Perdio==True:
                break