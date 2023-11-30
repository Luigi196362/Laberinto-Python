import cv2
import numpy as np
import os
import random



class GenerarEscenario():
    
    def GenerarImagenes():
        #Elegir cantidad de escenarios o numero aleatorio de escenarios 
        e=int (input ("Eliga una opcion: \n 1.- Escenarios personalizables \n 2.- Escenarios aleatorio \n\n"))
        if (e==1):
            
            #Verificar escenarios >= 2 y escenarios <= 10
            while True:
                os.system("cls")
                NumEscenarios= int (input("Ingresa el numero de escenarios: "))

                if (2<=NumEscenarios<=10):
                    break  
                else:  
                    if NumEscenarios<2:
                        print ("\nMuy pocos escenarios")
                    if NumEscenarios>10:
                        print ("\nDemasiados escenarios")
                    input()   
            
            while True:
                os.system("cls")
                Porcentaje= int (input("Ingresa el porcentaje de terreno caminable: "))

                if (65<=Porcentaje<=70):
                    break             
                else:  
                    if Porcentaje<65:
                        print ("\nPorcentaje muy pequeño")
                    if Porcentaje>70:
                        print ("\nPorcentaje muy alto")
                    input()
                
        else:        
            NumEscenarios=random.randint(2,10)
            Porcentaje=random.randint(65,70)
            
        os.system("cls")
        #Generar imagenes
        for i in range (NumEscenarios):
            print ("Generando imagen "+str(i+1)+"...")
            img = np.zeros((640, 600, 1), np.uint8)
            cv2.rectangle(img,pt1=(0,601),pt2=(640,640),color=50,thickness=-1)
            
            #Generar pasillos aleatorios
            #variables donde se guarda datos de x,y para comprobar que el conjunto no se repita 
            xreg=[]
            yreg=[]
            j=0
            #Generar numeros aleatorios
            while (j<Porcentaje):
                unico=True
                x= random.randrange(0,541,60)
                y= random.randrange(0,541,60)
                
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
                    cv2.rectangle(img,pt1=(x,y),pt2=(x+60,y+60),color=255,thickness=-1)
            #Colocar numero de escenario
            if (img[601,575]==255):
                cv2.putText(img,text="Escenario: {:.0f}".format(i+1),org=(2,630),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(0,0,0))
            else:
                cv2.putText(img,text="Escenario: {:.0f}".format(i+1),org=(2,630),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(255,255,255))
      
            #Colocar porcentaje de color blanco
            if (img[601,15]==255):
                cv2.putText(img,text="Porcentaje blanco: {:.0f}%".format(Porcentaje),org=(2,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(0,0,0))
            else:
                cv2.putText(img,text="Porcentaje blanco: {:.0f}%".format(Porcentaje),org=(2,615),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=.5,color=(255,255,255))
                  
            cv2.imwrite("Escenarios/Escenario "+str(i+1)+".jpg", img)
            
        print("Imagenes generadas")


