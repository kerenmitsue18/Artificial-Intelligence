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

MECANISMO DE SELECCION 
Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""
from Poblacion import Poblacion
from Individuo import Individuo
import numpy as np
import random 
class Seleccion:
    
    def seleccionaPadresIdx(self, poblacion, K=100):
        aptitudes = poblacion.fitnessPoblacion()
        idxWorst = poblacion.worst()# Valor mayor
        # Normalizar las aptitudes
        aptitudes = np.array(aptitudes)
        aptitudes = 1.-aptitudes/aptitudes[idxWorst]
        #Convierte las aptitudes en probabilidades usando softmax
        probs = np.exp(aptitudes)/np.sum(np.exp(aptitudes))
        #Elige K padres/madres
        return random.choices(list(range(len(probs))), weights=probs, k=K)
    
    def seleccionaPadres(self, poblacion, K=100):
        idx = self.seleccionaPadresIdx(poblacion, K)
        padres = Poblacion(poblacion.ff, poblacion.ciudades, 1)
        ind = []
        for i in range(K):
            ind.append(poblacion.poblacion[idx[i]])
        padres.poblacion = ind
        return padres
    
    def seleccionNatural(self, poblacion, K=100):
        idx = self.seleccionaPadresIdx(poblacion, K) #Elijo considerando la aptitud
        seleccionados = Poblacion(poblacion.ff,poblacion.ciudades, 1)
        seleccionados.poblacion = []
        for i in range(K):
            genes = poblacion.poblacion[i].genes.copy()
            ind = Individuo(poblacion.ciudades)
            ind.genes = genes
            seleccionados.poblacion.append(ind)
        return seleccionados
            
        
        