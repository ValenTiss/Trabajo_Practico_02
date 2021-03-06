import random 
from base import Generador_Datos
from sklearn.cluster import KMeans
from Clase_membresia import Membresia_de_cluster
from Clase_centroides  import Centroides
from Clase_graficador import Graficador
import numpy as np
from Clase_prueba import Pruebas

probador=Pruebas()
numero_de_prueba= input("Si desea una prueba rápida de las pruebas puestas en el documento presione 1,2,3 o 4. \n En caso contrario, si desea digitar manualmente los datos presione cualquier otro número: ")
try:
  numero_de_prueba=int(numero_de_prueba)
except:
  raise ValueError("La opción debe tiene que ser número un número entero")

numberSamplesPerClass= input("Ingese la cantidad de datos que desea crear: ")
try:
  numberSamplesPerClass=int(int(numberSamplesPerClass)/2)
except:
  raise ValueError("La cantidad de datos debe ser un número")

if numberSamplesPerClass > 0:
  if numero_de_prueba == 1:
    probador.prueba1(numberSamplesPerClass)
  elif numero_de_prueba == 2:
    probador.prueba2(numberSamplesPerClass)
  elif numero_de_prueba == 3:
    probador.prueba3(numberSamplesPerClass)
  elif numero_de_prueba == 4:
    probador.prueba4(numberSamplesPerClass)
  else:
    mean1_x= input("Ingese el dato mean1_x: ")
    mean1_y= input("Ingese el dato mean1_y: ")
    mean2_x= input("Ingese el dato mean2_x: ")
    mean2_y= input("Ingese el dato mean2_y: ")
    stds1_x= input("Ingese el dato stds1_x: ")
    stds1_y= input("Ingese el dato stds1_y: ")
    stds2_x= input("Ingese el dato stds2_x: ")
    stds2_y= input("Ingese el dato stds2_y: ")
    try:
      mean1_x= int(mean1_x)
      mean1_y= int(mean1_y)
      mean2_x= int(mean2_x)
      mean2_y= int(mean2_y)
      stds1_x= int(stds1_x)
      stds1_y= int(stds1_y)
      stds2_x= int(stds2_x)
      stds2_y= int(stds2_y)
    except:
      raise ValueError("Tipo de dato incorrecto, datos introducidos deben ser números")
    probador.prueba(numberSamplesPerClass, [mean1_x, mean1_y], [mean2_x,mean2_y], [stds1_x,stds1_y], [stds2_x,stds2_y])
else:
    raise ValueError("La cantidad de datos debe ser un número natural")
