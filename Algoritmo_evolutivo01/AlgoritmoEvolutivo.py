# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Algoritmo evolutivo completo 
PRUEBA DE FUNCIONAMIENTO
Created on Mon Aug 23 14:49:13 2021

ALGORITMO EVOLUTIVO COMPLETO
@author: KerenMitsue
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction
import numpy as np
import random

class AlgoritmoEvolutivo:
    
    def __init__(self, TAM_POB=100, GENERACIONES = 100):
        self.GENERACIONES = GENERACIONES
        self.poblacion = Poblacion(TAM_POB)
        self.ff = FitnessFunction()
        self.sel = Seleccion()
        self.TAM_POB = TAM_POB
    
    def evolve(self, GENERACIONES):
        
        for gen in range(self.GENERACIONES):

            # Elegir padres y madres
             K = int(len(self.poblacion.poblacion)/2)
             padres = self.sel.seleccionaPadres(self.poblacion, K)
             madres = self.sel.seleccionaPadres(self.poblacion, K)
             # print('Los padres son: \n', padres)
             # print('Las madres son:\n ', madres)
             
             # Cruza de los progenitores y produce hijos
             descendencia = []
             for mama, papa in zip(madres.poblacion, padres.poblacion):
                 hijo, hija = mama.cruza(papa)
                 descendencia.append(hijo)
                 descendencia.append(hija)
             
             hijos = Poblacion(1)
             hijos.poblacion = descendencia
             
             #Mutar al 5% de la descendencia
             mutar = int (np.ceil(len(hijos.poblacion)* 0.05))
             
             for i in range(mutar):
                 a = random.randint(0, len(hijos.poblacion)-1)
                 hijos.poblacion[a].mutar()
                 
                          
             # Unir a padres/madres + hijos
             generacion = []
             for i in range (len(self.poblacion.poblacion)):
                 generacion.append(self.poblacion.poblacion[i])
                 
             for i in range (len(hijos.poblacion)): # unir hijos
                 generacion.append(hijos.poblacion[i])
             
             nuevaGeneracion = Poblacion(1)
             nuevaGeneracion.poblacion = generacion
                         
             #Seleccionar self.TAM_POB individuos (Usar elitismo)
             SigGeneracion = self.sel.seleccionaPadres(nuevaGeneracion, self.TAM_POB)
             # print('La Siguiente generacion es: \n ', SigGeneracion)
             
             #Imprimir el mejor individuo*
             IndBest = []
             IndBest.append(SigGeneracion.poblacion[SigGeneracion.best()])
             best = Poblacion(1)
             best.poblacion = IndBest
             
             print('El mejor individuo hasta ahora es: ', best)
             
             self.poblacion.poblacion = SigGeneracion.poblacion
             
             
             
             
         
         
        