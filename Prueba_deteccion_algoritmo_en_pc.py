#Algoritmo de deteccion de las flechas según su color
#El programa se ejecuta y para finalizarlo se utiliza la tecla esc
#hay q iniciarlo de nuevo cada vez que se quiera analizar una flecha
#
#Detecta flecha verde para giro derecho y flecha azul para giro izquierdo 
 
import cv2
import numpy as np
 
#Inicia la camara 
captura = cv2.VideoCapture(0)
print ("Programa de procesamiento de imagen en PC")
empezar = ("Presione 1 para empezar a procesar")

if empezar == '1':
 
  while(1):
     
      #Capturamos una imagen y la convertimos de RGB -> HSV
      _, imagen = captura.read()
      hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
   
      #Establecemos el rango de colores que vamos a detectar
      #Verde oscuro a verde claro
      #azul oscuro a azul claro 
      verde_bajos = np.array([49,50,50], dtype=np.uint8)
      verde_altos = np.array([80, 255, 255], dtype=np.uint8)
      azul_bajos = np.array([100,65,75], dtype=np.uint8)
      azul_altos = np.array([130, 255, 255], dtype=np.uint8)
      
     #Crear una mascara con solo los pixeles dentro del rango de verdes
     #y crear una mascara con solo los pixeles dentro del rango de azules
      mask1 = cv2.inRange(hsv, verde_bajos, verde_altos)
      mask2 = cv2.inRange(hsv, azul_bajos, azul_altos)
 
     #Encontrar el area de los objetos que detecta la camara
     moments1 = cv2.moments(mask1)
     area1 = moments1['m00']
     moments2 = cv2.moments(mask2)
     area2 = moments2['m00']
 
      #Descomentar para ver el area por pantalla
      #print area
      if(area1 > area2):
         
          #Si el área es verde se realiza un giro a la derecha
          print ("Gire a la derecha")
          cv2.imshow('mascara', mask1)
          
      elif(area1 < area2):
      
          #Si el área es roja se realiza un giro a la izquierda
          print ("Gire a la izquierda")
          cv2.imshow('mascara', mask2)
      else:
          
          #Si no se determina que area es más grande hubo un error en el programa
          print ("Error en el procesamiento de la imagen")
     #Las siguientes lineas esperan a que se presione la tecla esc para terminar el programa
     tecla = cv2.waitKey(5) & 0xFF
     if tecla == 27:
         break
else:
  print ("Opcion invalida")
 
cv2.destroyAllWindows()
