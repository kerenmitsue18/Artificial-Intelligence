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
        
    
    