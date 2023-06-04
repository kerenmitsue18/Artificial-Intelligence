# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Primera version de un AE

Soluciona el problema f(x, y) = (x-1)^2 + (y+3)^2
Nota: Cada individuo es de 16 bits, 
8 para cada variable

POBLACION
Created on Mon Aug 23 14:57:59 2021

@author: KerenMitsue
"""
from Individuo import Individuo
from FitnessFunction import FitnessFunction
import numpy as np

class Poblacion:
    
    def __init__(self, TAM_POB=100):
        
        'Inicializa una poblacion'
        self.ff = FitnessFunction()
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo()
            i.inicializa()
            poblacion.append(i)
        self.poblacion = poblacion    
    
    def __str__(self):
        cad = ""
        aptitudes = self.fitnessPoblacion()
        for ind, aptitud in zip(self.poblacion, aptitudes):
            cad = cad + str(ind) + " FITNESS =  " + str(aptitud) + "\n"
        return cad
    
    def fitnessPoblacion(self):
        
        'Calcula la aptidud de todos los individuos de una poblacion'
        fp = []
        for ind in self.poblacion:
            fp.append(self.ff.fitness(ind))
        return fp
            
    #Elitismo: identificar al mejor individuo de una poblacion
    def best(self):
        'Regresa el índice del mejor individuo de una poblacion'
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.max(aptitudes))# Por que es negativo
    
    def worst(self):
        'Regresa el índice del peor individuo de una poblacion'
        aptitudes = self.fitnessPoblacion()
        return aptitudes.index(np.min(aptitudes))# Por que es negativo