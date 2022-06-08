# -*- coding: utf-8 -*-
"""K_means_base.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eXvk66XVovmnTxWJj5mJ9Wyn1Ykip2Mv
"""

from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np;
import pandas as pandas;
from scipy import ndimage
from torchvision import datasets, transforms
from torch.distributions import normal
from torch.distributions import multivariate_normal
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

"""## Manual example"""

class Agrupador_K_medias:
    def __init__(self, X, K = 2):
        #Matriz de pesos
        self.W = np.zeros(X.shape[0], K)
        #Se guardan los datos de manera global en X
        self.X = X
        #se definen los centroides como atributo
        self.Centroides = np.zeros(K, X.shape[1])
    
    
    

    def calcular_centroide_mas_cercano(self, Centroides, X, num_observacion):
        distancia_euclidiana_min = 9999
        num_centroide_mas_cercano = -1
        for i in range(0, Centroides.shape[0]):   
            vector_diferencia = Centroides[i, :] - X[0, :]    
            distancia_euclidiana = np.linalg.norm(vector_diferencia, 2)
            if(distancia_euclidiana < distancia_euclidiana_min):
                distancia_euclidiana_min = distancia_euclidiana
                num_centroide_mas_cercano = i
        return i
    
    def actualizar_W(self):
        #actualizar la matriz de pesos binarios W, de acuerdo a la pertenencia a los datos
        print("Por implementar")
        
    def actualizar_centroides(self):
        print("Por implementar")

def prueba_1():
    X = np.array([[50.0, 32], [42, 29], [80, 15], [70, 19]])
    print("Datos \n", X)
    #debe ser un valor aleatorio tomando en cuenta los minimos y maximos de de cada dimension
    Centroides = np.array([[50, 20.0], [70, 30]])
    print("Dimensiones en Centroides: ", Centroides.shape)
    print("Centroides iniciales \n", Centroides)
    print("centroide mas cercano de observacion 0 es el ", calcular_centroide_mas_cercano(Centroides, X, 0))
    print("centroide mas cercano de observacion 1 es el ", calcular_centroide_mas_cercano(Centroides, X, 1))

def prueba_2():
    X = np.array([[50.0, 32], [42, 29], [80, 15], [70, 19]])
    #debe ser un valor aleatorio tomando en cuenta los minimos y maximos de de cada dimension
    Centroides = np.array([[50, 20.0], [70, 30]])
    plt.scatter(X[:, 0], X[:, 1], marker = 'x')
    plt.scatter(Centroides[:, 0], Centroides[:, 1], marker = 'o')
    plt.show()
    Nuevos_centroides_1 = X[0:2, :].mean(axis = 0)
    Nuevos_centroides_2 = X[2:, :].mean(axis = 0)
    plt.scatter(X[:, 0], X[:, 1], marker = 'x')
    plt.scatter(Nuevos_centroides_1[0], Nuevos_centroides_1[ 1], marker = 'o')
    plt.scatter(Nuevos_centroides_2[0], Nuevos_centroides_2[ 1], marker = 'o')
    plt.show()
  

prueba_2()

"""## Creacion de los datos artificiales

Los datos son creados con una distribucion Gaussiana
"""

class Generador_Datos():

    def generar_datos(self, numberSamplesPerClass = 2, mean1 = [2, 2], mean2 = [26, 26], stds1 = [3, 3], stds2 = [2, 1]):
        """
        Creates the data to be used for training, using a GMM distribution
        @param numberSamplesPerClass, the number of samples per class
        @param mean1, means for samples from the class 1
        @param mean2, means for samples from the class 2
        @param stds1, standard deviation for samples, class 1
        @param stds2, standard deviation for samples, class 2    """
        means = torch.zeros(2)
        # Ones to concatenate for bias
        ones = torch.ones(numberSamplesPerClass, 1)
        means[0] = mean1[0]
        means[1] = mean1[1]
        # Covariance matrix creation with identity
        covarianceMatrix = torch.eye(2)
        covarianceMatrix[0, 0] = stds1[0]
        covarianceMatrix[1, 1] = stds1[1]
        samplesClass1 = self.__generar_datos_una_clase(means, covarianceMatrix, numberSamplesPerClass)
        means[0] = mean2[0]
        means[1] = mean2[1]
        covarianceMatrix[0, 0] = stds2[0]
        covarianceMatrix[1, 1] = stds2[1]
        samplesClass2 = self.__generar_datos_una_clase(means, covarianceMatrix, numberSamplesPerClass)
        # Concatenates the ones for the bias
       
        samplesAll = torch.cat((samplesClass1, samplesClass2), 0)
        #graficacion de los datos
        plt.scatter(samplesClass1[:, 0], samplesClass1[:, 1])
        plt.scatter(samplesClass2[:, 0], samplesClass2[:, 1], marker = 'x')
        plt.show()
       
        #Create targets
        targetsClass1 = torch.ones(numberSamplesPerClass, 1)
        targetsClass2 = -1 * torch.ones(numberSamplesPerClass, 1)
        targetsAll = torch.cat((targetsClass1, targetsClass2), 0)

        return (targetsAll.numpy(), samplesAll.numpy())


    '''
    Creates data with gaussian distribution
    '''
    def __generar_datos_una_clase(self, means, covarianceMatrix, numberSamples):
        # Inits the bi gaussian data generator
        multiGaussGenerator = multivariate_normal.MultivariateNormal(means, covarianceMatrix)
        # Takes the samples
        samples = multiGaussGenerator.sample(torch.Size([numberSamples]))

        return samples

"""## Probador del generador de datos"""

generador_datos = Generador_Datos()
(t, X) = generador_datos.generar_datos(numberSamplesPerClass = 200, mean1 = [12, 13], mean2 = [17, 17], stds1 = [3, 3], stds2 = [17, 17])
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(X)

"""## Pruebas para la TP 2"""

#generador_datos.generar_datos(numberSamplesPerClass = 200, mean1 = [12, 13], mean2 = [17, 17], stds1 = [3, 3], stds2 = [17, 17])
#generador_datos.generar_datos(numberSamplesPerClass = 200, mean1 = [2, 1], mean2 = [17, 17], stds1 = [3, 3], stds2 = [7, 7])
#generador_datos.generar_datos(numberSamplesPerClass = 100, mean1 = [12, 13], mean2 = [21, 22], stds1 = [3, 3], stds2 = [17, 17])
