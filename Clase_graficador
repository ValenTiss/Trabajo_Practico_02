import numpy as np;
import matplotlib.pyplot as plt
#import tkinter 
#from tkinter import messagebox

class Graficador:

  def grafico_clusters_centroides(self, sample1, sample2, centroide1_dibujar, centroide2_dibujar):
    plt.scatter(sample1[:, 0], sample1[:, 1], marker = 'o', label="Cluster 1")
    plt.scatter(sample2[:, 0], sample2[:, 1], marker = 'o', label="Cluster 2")
    plt.scatter(centroide1_dibujar[:, 0], centroide1_dibujar[:, 1], marker = 'o', c="red", label="Centroide 1")
    plt.scatter(centroide2_dibujar[:, 0], centroide2_dibujar[:, 1], marker = 'o', c="purple", label="Centroide 2")
    plt.xlabel("Abscisas")
    plt.ylabel("Ordenadas")
    plt.title("K-medias")
    plt.legend(loc="lower right")
    plt.show()
  
  
  """
  # def accion_de_boton():
  #   respuesta = messagebox.askyesno(message="Presione sí si desea ver los gráficos de k-medias hechos por Valentín y Federico, en caso contrario se mostrará el gráfico hecho en clase")
  #     if respuesta:
        
  def presionar_boton():
    ventana = tkinter.Tk()
    ventana.geometry("640x480")

    boton = tkinter.Button(text="Botón") #, command= accion_de_boton()
    boton.pack()
    ventana.mainloop()
  """
