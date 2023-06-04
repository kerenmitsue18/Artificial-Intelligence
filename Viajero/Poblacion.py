#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Poblacion al problema del agente viajero

POBLACION
Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""

from Individuo import Individuo
import numpy as np

class Poblacion:
    
    def __init__(self, ff, listaCiudades, TAM_POB=100):
        '''
        

        Parameters
        ----------
        ff : FitnessFuction
            Función aptitud de los individuos
        listaCiudades : list
            lista original de las ciudades
        TAM_POB : int
            Tamaño de la población

        Returns
        -------
        None.

        '''
        self.ff = ff
        self.ciudades = listaCiudades
        poblacion = []
        for i in range(TAM_POB):
            i = Individuo(listaCiudades)
            i.inicializa()
            poblacion.append(i)
        self.poblacion = poblacion    
    
    def __str__(self):
        cad = ""
        aptitudes = self.fitnessPoblacion()
        for ind, aptitud in zip(self.poblacion, aptitudes):
            cad=cad + str(ind) + " FITNESS =  " + str(-aptitud) + "\n"
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
        return aptitudes.index(np.max(aptitudes)) # retorna mejor aptitud
    
    def worst(self):
        'Regresa el índice del PEOR individuo de una poblacion'
        aptitudes = self.fitnessPoblacion()
        # CHECAR**************
        return aptitudes.index(np.min(aptitudes)) # retorna peor actitud