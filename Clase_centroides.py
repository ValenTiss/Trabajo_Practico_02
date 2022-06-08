

class Centroides:
  def __init__(self, x,y):
    self.__abscisas= x #Valor del centroide en el eje de las X
    self.__ordenadas= y #Valor del centroide en el eje de las Y
    self.__matriz_de_pertenecientes= [] #Matriz con los puntos que pertenecen al cluster del centroide 

  def agregregar_a_matriz(self, W, X, numero_centroide):
    """
    Si en 
    parametro1: matriz W
    parametro2: matrix X
    parametro3: 0 si es centroide1, 1 si es centroide 2. Representa la columna de W que está ligada al centroide
    """    
    for i in range(0,len(W)):
      if W[i][numero_centroide]==1:
        self.__matriz_de_pertenecientes+=[X[i]] 
  
  def getX(self):
    return self.__abscisas

  def getY(self):
    return self.__ordenadas

  def getMatriz(self):
    return self.__matriz_de_pertenecientes
