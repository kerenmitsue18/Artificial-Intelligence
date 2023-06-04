#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Representación para el problema de permutaciones
"Adivina la contraseña"


Created on Mon Sep 13 00:26:48 2021

@author: KerenMitsue
"""

import random
import numpy as np
class Individuo:
    
    def __init__(self):
        # Construye el alfabeto
        self.alfabeto = "abcdefghijklmnopqrstuvwxyz "
        # Alfabeto como una lista
        self.alfabetoList = [i for i in self.alfabeto]
        self.genes = []
        
    def inicializa(self, k=12):
        self.genes = random.choices(self.alfabetoList, k=k)
    
    def getPhenotype(self):
        return self.__str__()
        
    def getGenotype(self):
        return "[" + self.genes + "]"
    
    def __str__(self):
        cad = ""
        for c in self.genes:
            cad += c
        return cad
    
    # Mecanismos de variación
    def cruza(self, madre):
        '''Cruza por un punto'''
        mama = madre.genes
        papa = self.genes
        numGenes = len(papa)
        cp = int(numGenes/2) # Crosspoint
        genesHijo = mama[0:cp]
        genesHijo.extend(papa[cp:])
        genesHija = papa[0:cp]
        genesHija.extend(mama[cp:])
        hija = Individuo()
        hija.genes = genesHija
        hijo = Individuo()
        hijo.genes = genesHijo
        return [hija, hijo]
    
    def mutar(self):
        '''Reemplaza un caracter elegido de manera aleatoria'''
        total = len(self.genes)
        idx = np.random.randint(0, total)  # Indice del caracter a cambiar
        nuevo = random.choice(self.alfabeto)
        self.genes[idx] = nuevo  # Se reemplaza