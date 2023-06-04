#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Primera versión de un AE

Soluciona el problema adivina contraseña

ALGORITMO EVOLUTIVO COMPLETO
Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from Grafica import Grafica
import random
import numpy as np
class AlgoritmoEvolutivo:
    
    def __init__(self, ff, ciudades, points, TAM_POB=100, GENERACIONES = 100):
        self.GENERACIONES = GENERACIONES # Atributo GENERACIONES -> número de generaciones
        self.ciudades = ciudades # Atributo d -> número de variables
        self.TAM_POB = TAM_POB # Atributo TAM_POB -> tamaño de la población
        self.ff = ff # Atributo ff -> Objeto FitnessFunction
        self.sel = Seleccion() # Atributo sel -> Objeto Selección
        self.points = points
        self.grafica = Grafica()
        self.poblacion = Poblacion(self.ff, self.ciudades, self.TAM_POB) # Atributo TAM_POB -> tamaño de la población
        
        
    
    def evolve(self, GENERACIONES):
        
        for gen in range(self.GENERACIONES):

            # Elegir padres y madres
             K = int(len(self.poblacion.poblacion)/2) #Mitad de población será padres/madres
             padres = self.sel.seleccionaPadres(self.poblacion, K)
             madres = self.sel.seleccionaPadres(self.poblacion, K)

             # Cruza de los progenitores y produce hijos
             descendencia = []
             for mama, papa in zip(madres.poblacion, padres.poblacion):
                 hijo, hija = mama.cruza(papa) # Generar un hijo e hija
                 # Agregar hijos a la descendencia
                 descendencia.append(hijo) 
                 descendencia.append(hija)
             
             hijos = Poblacion(self.ff, self.ciudades, 1) #Convertir hijos a un objeto de tipo Población
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
             
             nuevaGeneracion = Poblacion(self.ff, self.ciudades, 1)
             nuevaGeneracion.poblacion = generacion
                   
             #Seleccionar self.TAM_POB individuos (Usar elitismo)
             SigGeneracion = self.sel.seleccionaPadres(nuevaGeneracion, self.TAM_POB)
             #Imprimir el mejor individuo
             IndBest = []
             IndBest.append(SigGeneracion.poblacion[SigGeneracion.best()]) 
             best = Poblacion(self.ff, self.ciudades, 1)
             best.poblacion = IndBest
             print('El mejor individuo hasta ahora es: ', best)
             
              # La siguiente generación será ahora la población
             self.poblacion.poblacion = SigGeneracion.poblacion 
             if (gen == GENERACIONES):
                 #tiene que graficar mejor individuo 
                 self.grafica.grafica(self.ciudades, self.points, IndBest[0])