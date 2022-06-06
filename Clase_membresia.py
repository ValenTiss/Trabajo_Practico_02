#importar la clase Centroides         ??? 
#Para calcular la raíz cuadrada
from numpy.ma.core import sqrt
import math


class Membresia_de_cluster:
  def __init__(self):
    self.__W=[] #matriz W
    self.__lista_centroides=[] #lista que contendrá parejas de centroides

  def agregar_centroides(self, pareja):
    """
    Agrega un nuevo par de centroides a lista_centroides
    """
    self.__lista_centroides.append(pareja)
  
  def calcular_w(self, centroide1, centroide2, X):
    for i in X:
      norma_centroide1 = self.calcular_norma(centroide1, i )
      norma_centroide2 = self.calcular_norma(centroide2, i )
      if(norma_centroide1 < norma_centroide2):
        self.__W.append([1,0])
      else:
        self.__W.append([0,1])

  def calcular_norma(self, centroide, lista):
    """
    Función que sirve para calcular la norma en R**2 o también conocida por distancia euclideana de un par ordenado (lista) a un centroide 
    parametro1: centroide
    parametro2: par ordenado 
    """ 
    return sqrt( (centroide.getX()-lista[0])**2 + (centroide.getY()-lista[1])**2 )

  def getW(self):
    return self.__W

  def getLista_centroides(self):
    return self.__lista_centroides

  def calcular_nuevo_centroide1(self, W,X):
    """
    Recalcula el centride 1 
    """
    sumatoria_numerador_abscisas= 0
    sumatoria_numerador_ordenadas=0
    sumatoria_denominador_abscisas= 0
    sumatoria_denominador_ordenadas= 0
    if(len(X)==len(W)):
      for i in range(0,len(X)):
        sumatoria_numerador_abscisas+= X[i][0]*W[i][0]
        sumatoria_numerador_ordenadas+=  X[i][1]*W[i][0]
        sumatoria_denominador_abscisas+= X[i][0]
        sumatoria_denominador_ordenadas+= X[i][1]
      nuevo_centroide1= Centroides( sumatoria_numerador_abscisas / sumatoria_denominador_abscisas , sumatoria_numerador_ordenadas/ sumatoria_denominador_ordenadas )
      return nuevo_centroide1
    else:
      raise ValueError("X y W no coinciden en tamaño")

  def calcular_nuevo_centroide2(self, W,X):
    """
    Recalcula el centride 2 
    """
    sumatoria_numerador_abscisas= 0
    sumatoria_numerador_ordenadas=0
    sumatoria_denominador_abscisas= 0
    sumatoria_denominador_ordenadas= 0
    if(len(X)==len(W)):
      for i in range(0,len(X)):
        sumatoria_numerador_abscisas+= X[i][0]*W[i][1]
        sumatoria_numerador_ordenadas+=  X[i][1]*W[i][1]
        sumatoria_denominador_abscisas+= X[i][0]
        sumatoria_denominador_ordenadas+= X[i][1]
      nuevo_centroide2= Centroides( sumatoria_numerador_abscisas / sumatoria_denominador_abscisas , sumatoria_numerador_ordenadas/ sumatoria_denominador_ordenadas )
      return nuevo_centroide2
    else:
      raise ValueError("X y W no coinciden en tamaño")
