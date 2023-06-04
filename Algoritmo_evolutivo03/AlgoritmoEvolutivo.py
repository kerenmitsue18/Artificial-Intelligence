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

Algoritmo Evolutivo completo
Created on Fri Sep 03 14:11:36 2021

@author: KerenMitsue
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction
from Graficar import Graficar 
from matplotlib import pyplot as plt
import numpy as np
import random

class AlgoritmoEvolutivo:
    
    def __init__(self, d, TAM_POB=100, GENERACIONES = 100):
        self.GENERACIONES = GENERACIONES # Atributo GENERACIONES -> número de generaciones
        self.d = d # Atributo d -> número de variables
        self.TAM_POB = TAM_POB # Atributo TAM_POB -> tamaño de la población
        self.poblacion = Poblacion(self.d, self.TAM_POB) # Atributo TAM_POB -> tamaño de la población
        self.ff = FitnessFunction() # Atributo ff -> Objeto FitnessFunction
        self.sel = Seleccion() # Atributo sel -> Objeto Selección
        
    
    def evolve(self, GENERACIONES):
        
        for gen in range(self.GENERACIONES):

            # Elegir padres y madres
             K = int(len(self.poblacion.poblacion)/2) #Mitad de población será padres/madres
             padres = self.sel.seleccionaPadres(self.d, self.poblacion, K)
             madres = self.sel.seleccionaPadres(self.d, self.poblacion, K)

             
             # Cruza de los progenitores y produce hijos
             descendencia = []
             for mama, papa in zip(madres.poblacion, padres.poblacion):
                 hijo, hija = mama.cruza(papa) # Generar un hijo e hija
                 # Agregar hijos a la descendencia
                 descendencia.append(hijo) 
                 descendencia.append(hija)
             
             hijos = Poblacion(self.d, 1) #Convertir hijos a un objeto de tipo Población
             hijos.poblacion = descendencia
             
             #Mutar al 5% de la descendencia
             mutar = int (np.ceil(len(hijos.poblacion)* 0.05)) # Número de hijos a mutar
             for i in range(mutar):
                 a = random.randint(0, len(hijos.poblacion)-1)
                 hijos.poblacion[a].mutar() #Mutación de hijo
                 
                          
             # Unir a padres/madres + hijos
             generacion = []
             for i in range (len(self.poblacion.poblacion)): # Unión de padres
                 generacion.append(self.poblacion.poblacion[i])
                 
             for i in range (len(hijos.poblacion)): # Unión de hijos
                 generacion.append(hijos.poblacion[i])
             
             nuevaGeneracion = Poblacion(self.d, 1)
             nuevaGeneracion.poblacion = generacion
                         
             #Seleccionar self.TAM_POB individuos (Usar elitismo)
             SigGeneracion = self.sel.seleccionaPadres(self.d, nuevaGeneracion, self.TAM_POB)
             
             #Imprimir el mejor individuo
             IndBest = []
             IndBest.append(SigGeneracion.poblacion[SigGeneracion.best()]) 
             best = Poblacion(self.d, 1)
             best.poblacion = IndBest
             print('El mejor individuo hasta ahora es: ', best)
             
             #Si número de variables es 2 -> Graficar
             if(self.d == 2):
                 self.graficar = Graficar(gen); # Objeto de tipo graficar
                 # Graficar individuos de una población
                 for i in range(len(self.poblacion.poblacion)):
                    punto = self.poblacion.poblacion[i].getPhenotype() #Obtener fenotipo del individuo
                    x = punto[0]
                    y = punto[1]
                    z = self.ff.fitness(self.poblacion.poblacion[i])
                    self.graficar.graficarInd(x,y,z)                 
             
             # La siguiente generación será ahora la población
             self.poblacion.poblacion = SigGeneracion.poblacion 
             
             
             
             
         
         
        