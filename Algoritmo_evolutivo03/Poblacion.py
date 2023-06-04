# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
    Encontrar el minimo de la siguiente función:
        f(x) = 10d + sumatoria de i = 1 hasta d ( xi^2 - 10cos(2*pi*xi))
    
    Población 
Created on Fri Sep 03 14:11:36 2021

@author: KerenMitsue
"""
from Individuo import Individuo
from FitnessFunction import FitnessFunction
import numpy as np

class Poblacion:
    
    def __init__(self, d, TAM_POB=100):
        self.d = d #Atributo d -> número de variables
        'Inicializa una poblacion'
        self.ff = FitnessFunction() # Atributo ff -> Objeto de tipo FitnessFuction
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo(d) # Crea individuo
            i.inicializa(d) # Inicializa individuo
            poblacion.append(i) #Agregar a un arreglo
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