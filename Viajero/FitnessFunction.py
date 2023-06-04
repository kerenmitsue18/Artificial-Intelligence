#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Función de aptitud para el problema del agente viajero.
Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""

import numpy as np

class FitnessFunction:
    
    def __init__(self, distancias, ciudades):
        '''
        

        Parameters
        ----------
        distancias : list
            lista de distancias entre ciudades
        ciudades : list
            lista original de las ciudades

        Returns
        -------
        None.

        '''
        self.distancias = distancias
        self.ciudades = ciudades
        
    def maximaDistancia(self):
        maxDist = -1
        for lista in self.distancias:
            for distancia in lista:
                if distancia > maxDist:
                    maxDist = distancia #maxima distancia entre ciudades
        return maxDist
    
    def distance(self, cityA, cityB):
        iA = self.ciudades.index(cityA) # indice de ciudad A
        iB = self.ciudades.index(cityB) # indice de ciudad B
        indice0 = iA
        indice1 = iB
        if iA > iB: # Si existe la distancia
            pass
        elif iA == iB: # Si la ciudad es si misma, entonces la disrancia es 0
            indice0 = 0
            indice1 = 0
        else: #No existe la distancia
            indice0 = iB
            indice1 = iA
        return self.distancias[indice0][indice1]
        
    def fitness(self, individuo):
        freqs = individuo.frecuencyTable()
        sum = 0
        # Realizar penalizacion a individuos invalidos
        for i in freqs:
            sum += np.abs(freqs[i] - 1)
        penalizacion = sum * self.maximaDistancia()
        
        # Calcular la suma del recorrido
        recorrido = 0;
        cityA = individuo.genes[0]
        for i in range (0, len(individuo.genes)-1):
                cityB = individuo.genes[i+1]
                recorrido += self.distance(cityA, cityB)
                cityA = cityB
                
        #Calcular recorrido al punto inicial
        cityA = individuo.genes[0]
        recorrido += self.distance(cityA, cityB)
        
        return -(recorrido + penalizacion) #retornar fitness
            
                
            
        
        
        
            