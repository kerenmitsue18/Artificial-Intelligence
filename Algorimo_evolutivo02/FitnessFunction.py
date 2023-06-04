#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Función de aptitud para el problema de adivina contraseña
Regresa el número de coincidencias entre el objetivo y el individuo.
Futuro: Regresa la posición de las coindicencias


Created on Mon Sep 13 00:26:48 2021

@author: KerenMitsue
"""

from Individuo import Individuo
import numpy as np
class FitnessFunction:
    
    def __init__(self, objetivo):
        '''Función objetivo para el problema "Adivina contraseña".
        objetivo: Una cadena
        '''
        self.objetivo = objetivo
        
    def fitness(self, individuo):
        coincidencias = 0
        i = 0
        #futuro = np.zeros(len(self.objetivo)) # Siguiente versión
        for letra in individuo.genes:
            if self.objetivo[i] == letra:
                coincidencias += 1
                #  futuro[i] = 1. # Siguiente versión
            i += 1
        return coincidencias
            