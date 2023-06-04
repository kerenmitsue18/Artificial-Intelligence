# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 

Created on Thu Sep 16 16:28:33 2021

@author: KerenMitsue
"""
from matplotlib import pyplot as plt
import numpy as np
class Grafica: 
    
    def __init__(self):
        fig, axs = plt.subplots(1)
        self.fig = fig
        self.axs = axs
        plt.xlim(0,10)
        plt.ylim(0,10)
            
    def generapuntos(self, tam):
        points = self.fig.ginput(tam)
        points = np.array(points)
        self.axs.plot(points[:,0], points[:,1] ,'or')
        plt.show()
        plt.close(self.fig)
        return points
        
    
    def grafica(self, ciudades, puntos, ind):
        self.axs.plot(puntos[:,0], puntos[:,1] ,'or')
        solucion = ind.genes
        idx = []
        for i in range(len(ciudades)):
            ciudad = ciudades[i]
            iCiudad = solucion.index(ciudad) 
            idx.append(iCiudad)
        print(idx)
        x = [puntos[0][0], puntos[1][0]]
        for i in range (len(ciudades)):
            y = [puntos[i][1], puntos[i+1][1]]
            x = y            
            plt.plot(x, y, "-b")
        x = [puntos[0][0], puntos[1][0]]
        plt.plot(x, y, "-b")
        plt.show()
    
    