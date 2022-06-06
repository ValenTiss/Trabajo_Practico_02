#Para generar primeros centroides
import random 

def calcular_indices_random(X):
  return random.randint(0, len(X-1 )






#Se generan datos, esto es del profe
generador_datos = Generador_Datos()
(t, X) = generador_datos.generar_datos(numberSamplesPerClass = 200, mean1 = [2, 3], mean2 = [6, 6], stds1 = [3, 3], stds2 = [4, 3])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)





#Se calculan los primeros centroides
membresia= Membresia_de_cluster()
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
P = 3 #cantidad de iteraciones  ??? cambiar a input y verificar que sea numero
for i in range(P):
  pareja_centorides =  membresia.getLista_Centroides()[i]
  W = membresia.calcular_w( pareja_centroides[0], pareja_centroides[1], X)
  #Se genera la lista de matriz_de_pertenecientes de cada centroide
  pareja_centroides[0].agregregar_a_matriz( W, X, 0)
  pareja_centroides[1].agregregar_a_matriz( W, X, 1)
  #??? aquí ya tenemos lo que se necesita para el gráfico


  #Se crean los nuevos centroides 
  membresia.agregar_centroides([ membresia.calcular_nuevo_centroide1(W,X) , membresia.calcular_nuevo_centroide1(W,X)])
