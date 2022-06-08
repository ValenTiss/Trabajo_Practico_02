#Para generar primeros centroides
import random 
from base import Generador_Datos
from sklearn.cluster import KMeans
from Clase_membresia import Membresia_de_cluster
from Clase_centroides  import Centroides
from Clase_graficador import Graficador
import numpy as np

def calcular_indices_random(X):
  return random.randint(0, len(X)-1 )



#Se generan datos, esto es del profe
generador_datos = Generador_Datos()
(t, X) = generador_datos.generar_datos(numberSamplesPerClass = 200, mean1 = [2, 3], mean2 = [6, 6], stds1 = [3, 3], stds2 = [4, 3])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)
#print("Resultado kmeans: ", kmeans.labels_)




#Se calculan los primeros centroides
membresia= Membresia_de_cluster()
graficador= Graficador()
#graficador.presionar_boton()

#Matriz de datos
X = (t, X)[1] 
#Se calculan aleatoriamente dos indices de la matriz de datos para generar los primeros centroides
numero_aleatorio1 = calcular_indices_random(X)
numero_aleatorio2 = calcular_indices_random(X)
#Se verifica que los dos números aleatorios no sean el mismo
while numero_aleatorio1 == numero_aleatorio2:
  numero_aleatorio2 = calcular_indices_random(X)
#Se inicializan los primeros centroides
centroide1= Centroides(X[numero_aleatorio1][0], X[numero_aleatorio1][1])
centroide2= Centroides(X[numero_aleatorio2][0], X[numero_aleatorio2][1])
#Se agregan los centorides a la lista de centroides
membresia.agregar_centroides([centroide1,centroide2])
P =  7 #cantidad de iteraciones  ??? cambiar a input y verificar que sea numero
for i in range(P):
  pareja_centroides =  membresia.getLista_centroides()[i]
  actual_centroide1= pareja_centroides[0]
  actual_centroide2= pareja_centroides[1]
  W = membresia.calcular_w( actual_centroide1, actual_centroide2, X)
  #Registra si un centroide no se relaciona con nadie
  bandera=0
  for j in W:
    bandera+=j[0]
  if bandera==0 or bandera==len(W):
    print("Un centroide no se relaciona con nadie")
    break 
  #Se genera la lista de matriz_de_pertenecientes de cada centroide
  actual_centroide1.agregregar_a_matriz( W, X, 0)
  actual_centroide2.agregregar_a_matriz( W, X, 1)
  sample1= np.array(actual_centroide1.getMatriz(), dtype=object)
  sample2= np.array(actual_centroide2.getMatriz(), dtype=object)
  centroide1_dibujar= np.array([[actual_centroide1.getX(), actual_centroide1.getY()]], dtype=object)
  centroide2_dibujar= np.array([[actual_centroide2.getX(), actual_centroide2.getY()]], dtype=object)
  #??? aquí ya tenemos lo que se necesita para el gráfico


  graficador.grafico_clusters_centroides(sample1, sample2, centroide1_dibujar, centroide2_dibujar)
  
  
  T= membresia.calcular_T(W)
  resultado=np.array([[T],X], dtype=object)
  print("En la iteración", i+1 ," se tuvo una tasa de error de ", membresia.calcular_tasa_error(kmeans.labels_, T), " respecto al arreglo de etiquetas T.")
  #Se crean los nuevos centroides 
  membresia.agregar_centroides([ membresia.calcular_nuevo_centroide1(W,X) , membresia.calcular_nuevo_centroide2(W,X)])
  
