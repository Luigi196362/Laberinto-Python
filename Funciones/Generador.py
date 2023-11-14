import cv2
import numpy as np
import os
import random

class GenerarEscenario():
    #Verificar escenarios >= 2 y escenarios <= 10

    def verificacion():
        os.system("cls")
        N= int (input("Ingresa el numero de escenarios: "))
        if (2<=N<=10):
            print ("Generando imagenes...")
            return N
        else:
            if(N<2):
                print ("Muy pocos escenarios")
            if (N>10):
                print ("Demasiados escenarios")  
            input()
            return GenerarEscenario.verificacion()

    def GenerarImagenes():
        #Elegir cantidad de escenarios o numero aleatorio de escenarios 
        e=int (input ("Eliga una opcion: \n 1.- Elegir numero entre 2 y 10 \n 2.- Numero aleatorio \n\n"))
        if (e==1):
            n=GenerarEscenario.verificacion()
        else:
            os.system("cls")
            print("Generando numero aleatorio de escenarios...")
            n=random.randint(2,10)
        
        #Generar imagenes
        for i in range (n):
            i=i+1
            print ("Generando imagen "+str(i)+"...")
            img = np.zeros((600, 600, 1), np.uint8)
            cv2.rectangle(img,pt1=(0,0),pt2=(599,599),color=(250,250,250))
            
            #Generar pasillos aleatorios
            #variables donde se guarda datos de x,y para comprobar que el conjunto no se repita 
            xreg=[]
            yreg=[]
            j=0
            #Generar numeros aleatorios
            while (j<65):
                unico=True
                x= random.randrange(0,541,60)
                y= random.randrange(0,541,60)
                
                #Si la longitud de las listas es 0 entonces añadir los primeros numeros aleatorios
                if (len(xreg)== 0 and len(yreg)==0):
                    xreg.append(x)
                    yreg.append(y)
                else:
                    #verificar si el conjunto de coordenadas ya extiste en el registro
                    for k in range (len (xreg)):
                        if ((x== xreg[k]) and (y==yreg[k])):
                            unico=False
                            break
                #si es unico se registra,pinta la zona y suma un numero al contador
                if (unico==True):
                    j+=1
                    xreg.append(x)
                    yreg.append(y)
                    cv2.rectangle(img,pt1=(x,y),pt2=(x+60,y+60),color=(250,250,250),thickness=-1)
                                
            #Colocar numero de escenario
            if (img[575,580]==250):
                cv2.putText(img,text=str(i),org=(575,590),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(0,0,0))
            else:
                cv2.putText(img,text=str(i),org=(575,580),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(250,250,250))
            cv2.imwrite("Escenarios/Escenario "+str(i)+".jpg", img)
        print("Imagenes generadas")
