# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Primera versión de un AE

Soluciona el problema f(x, y) = (x-1)^2 + (y+3)^2
Nota: Cada individuo es de 16 bits, 
8 para cada variable

MECANISMO DE SELECCION

Created on Mon Aug 23 15:16:48 2021

@author: KerenMitsue
"""
from Poblacion import Poblacion
from Individuo import Individuo
from FitnessFunction import FitnessFunction
import numpy as np
import random 

class Seleccion:
    
        
    def seleccionaPadresIdx(self, d,  poblacion, K=100):
        self.d = d
        aptitudes = poblacion.fitnessPoblacion()
        idxWorst = poblacion.worst()# Valor mayor
        # Normalizar las aptitudes
        aptitudes = np.array(aptitudes)
        aptitudes = 1.-aptitudes/aptitudes[idxWorst]
        #Convierte las aptitudes en probabilidades usando softmax
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        #Elige K padres/madres
        return random.choices(list(range(len(probs))), weights=probs, k=K)
        
    
    def seleccionaPadres(self, d,  poblacion, K=100):
        idx = self.seleccionaPadresIdx(d, poblacion, K) #Indice de los mejores padres
        padres = Poblacion(d, 1)
        ind = []
        for i in range(K):
            ind.append(poblacion.poblacion[idx[i]]) #Agregar a un arreglo
        padres.poblacion = ind
        return padres #Retornar padres
    

        
    