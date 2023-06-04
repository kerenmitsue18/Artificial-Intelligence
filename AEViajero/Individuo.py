#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Rampirez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Representación para el problema del agente viajero (TSP: Traveling
                                                                 Salesman 
                                                                 Problem)
Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""

import random
import collections 
import operator

class Individuo:
       
    def __init__(self, listaCiudades):
        '''
        
        Parameters
        ----------
        listaCiudades : list
            Lista de las ciudades a recorrer, no deben haber repeticiones.
        Returns
        -------
        None.
        '''
        self.ciudades = listaCiudades
        self.genes = []
        
    def inicializa(self):
        numCiudades = len(self.ciudades)
        self.genes = random.sample(self.ciudades, numCiudades)
    
    def getPhenotype(self):
        return self.genes
        
    def getGenotype(self):
        ruta = "Recomended path: " + self.__str__()
        return ruta
    
    def __str__(self):
        cad = ""
        for cd in self.genes:
            cad += cd
            cad += " -> "
        cad += self.genes[0]   # Regresa al punto de partida  
        return cad
    
    def frecuencyTable(self):
        return collections.Counter(self.genes)
    
    # Mecanismos de variación
    def cruza(self, madre):
        #Cruza por un punto 
        mama = madre.genes
        papa = self.genes
        limit = int(len(self.genes)/2)
        hijo = papa[0:limit]
        hijo.extend(mama[limit:])
        hija = mama[0:limit]
        hija.extend(papa[limit:])
        
        #Los hijos los convertimos a individuos
        hijaObj = Individuo(self.ciudades)
        hijaObj.genes = hija
        hijaObj.frecuency = hijaObj.frecuencyTable()
        hijoObj = Individuo(self.ciudades)
        hijoObj.genes = hijo
        hijoObj.frecuency = hijoObj.frecuencyTable()
        
        return hijoObj, hijaObj
    
        """
        # determinar si las frecuencias son mayores a 1
        if hijaObj.frecuency.values() is not None:
            self.preventive(hijaObj)
        if hijoObj.frecuency.values() is not None:
            self.preventive(hijoObj)
        """
        
     
    """
    def preventive(self, ind):  
        print('genes del individuo', ind.genes)
        valores = list(ind.frecuency.keys())
        indices = list(ind.frecuency.values())
        ciudad  = random.sample(self.ciudades, 1)
       
        for i in range (len(ind.genes)):
            for j in range (len(ind.genes)):
                if(ind.genes[i] == ind.genes[j]):
                     while ind.genes.__contains__(ciudad[0]):
                         ciudad  = random.sample(self.ciudades, 1)
                     print(ciudad[0])
                     ind.genes[j] == ciudad[0]
                print(ind.genes)

        
        print("Genes que se previnieron errores", ind.genes) 
     """                  
     
    def mutar(self):
        indices = random.sample(range(len(self.genes)), 2)
        temp = self.genes[indices[0]]
        self.genes[indices[0]] = self.genes[indices[1]]
        self.genes[indices[1]] = temp
        
