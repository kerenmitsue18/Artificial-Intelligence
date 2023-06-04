# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Primera versión de un AE

Soluciona el problem f(x,y) = (x-1)^2 + (y+3)^2
Notas: cada invididuo es de 16 bits,
8 para caa variable

Created on Mon Aug 23 14:11:36 2021

@author: KerenMitsue
"""

import random
class Individuo:
    
    def inicializa(self, k=16):
        self.genes = random.choices([0, 1], k=k)
    
    def getPhenotype(self):
        # Separo x y y
        x = self.genes[0:8]
        y = self.genes[8:]
        
        # calculo los signos
        if x[0] == 0:
            signoX = +1
        else:
            signoX = -1            

        if y[0] == 0:
            signoY = +1
        else:
            signoY = -1
            
        # Convertir a cadena  x, y
        x = str(x[1:])
        x = x.replace('[','')
        x = x.replace(',','')
        x = x.replace(']','')
        x = x.replace(' ','')
        y = str(y[1:])
        y = y.replace('[','')
        y = y.replace(',','')
        y = y.replace(']','')
        y = y.replace(' ','')        
        x = int(x, 2)*signoX*5./127.
        y = int(y, 2)*signoY*5./127.
        return [x, y]        
    
    # Representación del individuo
    def getGenotype(self): 
        return str(self.genes)
    
    def __str__(self):
        x, y = self.getPhenotype()
        return self.getGenotype() + " -> " + "x={:.4f}, y={:.4f}".format(x,y)
    
    #Mecanismos de variacion
    def cruza(self, madre):
        #Cruza por un punto
        mama = madre.genes
        papa = self.genes
        hijo = papa[0:8]
        hijo.extend(mama[8:])
        hija = mama[0:8]
        hija.extend(papa[8:])
        
        #En este momento los hijos son listas, no individuos
        hijaObj = Individuo()
        hijaObj.genes = hija
        hijoObj = Individuo()
        hijoObj.genes = hijo
        return [hijoObj, hijaObj]
        
        
    
    def mutar(self):
        #Mutacion extrema: Cambia todo el individuo
        self.genes = random.choices([0,1], k= len(self.genes))
    

