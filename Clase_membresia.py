#importar la clase Centroides         ??? 
#Para calcular la raíz cuadrada
from numpy.ma.core import sqrt
import math
from Clase_centroides import Centroides

class Membresia_de_cluster:
  def __init__(self):
    self.__lista_centroides=[] #lista que contendrá parejas de centroides

  def calcular_T(self, W):
    T=[]
    for i in W:
      if i[0] == 1:
        T+=[0]
      else:
        T+=[1]
    return T  
  
  
  def agregar_centroides(self, pareja):
    """
    Agrega un nuevo par de centroides a lista_centroides
    """
    self.__lista_centroides.append(pareja)
  
  def calcular_w(self, centroide1, centroide2, X):
    W=[]
    for i in X:
      norma_centroide1 = self.calcular_norma(centroide1, i )
      norma_centroide2 = self.calcular_norma(centroide2, i )
      if(norma_centroide1 < norma_centroide2):
        W.append([1,0])
      else:
        W.append([0,1])
    return W

  def calcular_norma(self, centroide, lista):
    """
    Función que sirve para calcular la norma en R**2 o también conocida por distancia euclideana de un par ordenado (lista) a un centroide 
    parametro1: centroide
    parametro2: par ordenado 
    """ 
    return sqrt( (centroide.getX()-lista[0])**2 + (centroide.getY()-lista[1])**2 )

  def getLista_centroides(self):
    return self.__lista_centroides

  def calcular_nuevo_centroide1(self, W,X):
    """
    Recalcula el centride 1 
    """
    sumatoria_numerador_abscisas= 0
    sumatoria_numerador_ordenadas=0
    sumatoria_denominador= 0
    if(len(X)==len(W)):
      for i in range(0,len(X)):
        sumatoria_numerador_abscisas+= X[i][0]*W[i][0]
        sumatoria_numerador_ordenadas+=  X[i][1]*W[i][0]
        sumatoria_denominador+= W[i][0]
      nuevo_centroide1= Centroides( sumatoria_numerador_abscisas / sumatoria_denominador , sumatoria_numerador_ordenadas/ sumatoria_denominador )
      return nuevo_centroide1
    else:
      raise ValueError("X y W no coinciden en tamaño")

  def calcular_nuevo_centroide2(self, W,X):
    """
    Recalcula el centride 2 
    """
    sumatoria_numerador_abscisas= 0
    sumatoria_numerador_ordenadas=0
    sumatoria_denominador= 0
    if(len(X)==len(W)):
      for i in range(0,len(X)):
        sumatoria_numerador_abscisas+= X[i][0]*W[i][1]
        sumatoria_numerador_ordenadas+=  X[i][1]*W[i][1]
        sumatoria_denominador+= W[i][1]
      nuevo_centroide2= Centroides( sumatoria_numerador_abscisas / sumatoria_denominador , sumatoria_numerador_ordenadas/ sumatoria_denominador )
      return nuevo_centroide2
    else:
      raise ValueError("X y W no coinciden en tamaño")

  def calcular_tasa_error(self, correcto, T):
    acumulado=0
    for i in range(0,len(correcto)):
      if correcto[i] - T[i] != 0:
        acumulado+= 1
    return  ( acumulado/len(correcto) )
