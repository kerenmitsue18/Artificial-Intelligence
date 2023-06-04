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

Created on Mon Sep 13 00:26:48 2021

@author: KerenMitsue
"""

from Individuo import Individuo
from Poblacion import Poblacion
from Seleccion import Seleccion
from FitnessFunction import FitnessFunction
import random
import numpy as np
class AlgoritmoEvolutivo:
    
    def __init__(self, funcionAptitud, TAM_POB=100, GENERACIONES=300):
        '''
        Constructor para un AE que resuelve el problema de encontrar 
        una cadena de caracteres.
        
        Parameters
        ----------
        funcionAptitud : FitnessFunction
            Clase que implementa el método fitness()
        TAM_POB : int, optional
            Número de individuos en la población. The default is 100.
        GENERACIONES : int, optional
            Total de generaciones en la evolución. The default is 300.

        Returns
        -------
        None.
        '''
        self.GENERACIONES = GENERACIONES
        self.poblacion = Poblacion(funcionAptitud, TAM_POB)
        self.ff = funcionAptitud
        self.sel = Seleccion()

    def evolve(self, GEN=1):
        for gen in range(GEN):
            # Elegir padres/madres
            K = int(len(self.poblacion.poblacion)/2)
            padres = self.sel.seleccionaPadres(self.poblacion, K)
            madres = self.sel.seleccionaPadres(self.poblacion, K)
            # Cruza los progenitores y produce hijos
            descendencia = []
            for mama, papa in zip(madres.poblacion, padres.poblacion):
                hijo, hija = mama.cruza(papa)
                descendencia.append(hija)
                descendencia.append(hijo)
            # Mutar al 5% de la descendencia
            hijos = Poblacion(self.ff, 1)
            hijos.poblacion = descendencia
            # Calcula el 5% del tamaño de la población
            totalMutar = np.ceil(len(hijos.poblacion)*0.05)
            # Muta a algunos individuos seleccionados estocásticamente.
            # Seleccionar self.TAM_POB individuos (usar elitismo)
            for i in range(int(totalMutar)):
                idx = random.randrange(0, len(hijos.poblacion))
                hijos.poblacion[idx].mutar()            
            # Unir  padres/madres + hijos
            #self.poblacion.poblacion unir con hijos
            nuevaGeneracion = []
            for ind in self.poblacion.poblacion:
                nuevaGeneracion.append(ind) # Padres/Madres
            for ind in hijos.poblacion:
                nuevaGeneracion.append(ind) # Hijos
            temp = Poblacion(self.ff, 1)
            temp.poblacion = nuevaGeneracion
            nuevaGeneracion = temp

            # Seleccionar self.TAM_POB individuos (usar elitismo)
            # Mecanismo de elitismo
            idxBest = nuevaGeneracion.best() # El mejor individuo hasta ahora
            sigGeneracion = Poblacion(self.ff,1)
            sigGeneracion.poblacion = [] #Empieza vacía
            IndividuoDeElite = Individuo()
            IndividuoDeElite.genes = nuevaGeneracion.poblacion[idxBest].genes.copy()
            sigGeneracion.poblacion.append(IndividuoDeElite) # Elitismo
            
            # Seleccionar N-1 individuos, que estarán en la siguiente generación
            temp = self.sel.seleccionNatural(nuevaGeneracion, len(self.poblacion.poblacion)-1)
            for item in temp.poblacion:
                sigGeneracion.poblacion.append(item)
                
            # Imprimir el mejor individuo*
            print("Best solution until now:")
            idxBest = sigGeneracion.best() # El mejor individuo hasta ahora
            print(sigGeneracion.poblacion[idxBest])
            print(self.ff.fitness(sigGeneracion.poblacion[idxBest]))
            self.poblacion.poblacion = sigGeneracion.poblacion #Nos quedamos con esta
            
            #Termina si llega al objetivo
            idx = self.poblacion.best()
            if self.poblacion.poblacion[idx].__str__() == self.ff.objetivo:
                return