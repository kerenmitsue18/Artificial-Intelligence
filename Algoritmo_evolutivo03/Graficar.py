"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
    Encontrar el minimo de la siguiente función:
        f(x) = 10d + sumatoria de i = 1 hasta d ( xi^2 - 10cos(2*pi*xi))

Graficar evolución cuando son dos variables
Created on Fri Sep 03 14:11:36 2021
@author: KerenMitsue
"""

import numpy as np
from matplotlib import pyplot as plt

class Graficar:
    
    def __init__(self, gen):
        
        # Graficar función
        x = np.arange(-6,6,0.1)
        y = np.arange(-6,6,0.1)
        X, Y = np.meshgrid(x,y,sparse = False, indexing = 'ij')
        Z = self.f(X, Y)
                                
        # Graficar figura
        fig = plt.figure()
        title = "Generacion {:1}".format(gen+1)
        ax = plt.axes(projection='3d')
        ax.contour3D(x,y,Z, 50, cmap = 'viridis')
                 
        # Modificar etiquetas en ejes
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_title(title)
                 
    def f(self, x,y):
        # Función en dos variables (3D)
        return 20 + (np.square(x) -(10 * np.cos(2 * np.pi * x ))) + (np.square(y) -(10 * np.cos(2 * np.pi * y )))
        
    def graficarInd(self, x,y, z):
        plt.plot(x,y,z,'o', color = "red") # Grafica los individuos
        
        