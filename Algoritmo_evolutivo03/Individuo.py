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
Created on Fri Sep 03 14:11:36 2021

Individuo de una función
@author: KerenMitsue
"""

import random # Importar clase random

class Individuo:
    
    def __init__(self, d = 2):
        self.d = d # Atributo d -> número de variables
        
    def inicializa(self, d=2, k=8):
        self.genes = random.choices([0, 1], k= d*k) # Genes del individuo
    
    def getPhenotype(self):
        
        # Separo xi genes 
        xi = []
        start = 0
        limit = 8
        for i in range(self.d):
            x = self.genes[start:limit] # genes desde start hasta limit
            xi.append(x) # Almacenar en arreglo xi
            start = limit
            limit += 8    
        
        # El mímimo se encuentra entre (-5,5)
        # Si va de -5 a 5  con 2^(n-1) -> 5/127
        # Convertir a cadena  x, y
        for i in range (len(xi)):
            
            # calculo los signos
            if xi[i][0]== 0:
                signoXi = +1
            else: 
                signoXi = -1
            # Modificando la cadena de los genes
            xi[i] = str(xi[i][1:])
            xi[i] = xi[i].replace('[', '')  
            xi[i] = xi[i].replace('[','')
            xi[i] = xi[i].replace(',','')
            xi[i] = xi[i].replace(']','')
            xi[i] = xi[i].replace(' ','')
            xi[i] = int(xi[i], 2) * signoXi * 5./127 # convertir cadena de 1,0 en valor numérico
        return xi       
    
    
    # Representación del individuo
    def getGenotype(self): 
        return str(self.genes)
    
    # Representación en cadena del individuo
    def __str__(self):
        x = self.getPhenotype() # Obtener fenotipo
        cad = self.getGenotype() + "-> "
        for i in range (len(x)):
            cad += "X{:1} = {:.4f}".format(i+1,x[i]) + " "
        return cad
    
    #Mecanismos de variacion
    def cruza(self, madre):
        
        #Cruza por dos puntos
        mama = madre.genes
        papa = self.genes

        # Si len(genes) es divisible entre 3 -> la cantidad de 0 y 1 será igual para 
        # cada sección del individuo
        if len(self.genes) % 3 == 0 :
            limit = int(len(self.genes)/3)
            #Cruza para el hijo
            hijo = papa[0:limit]
            hija = mama[0:limit]
            limit2 = limit + limit
            hijo.extend(mama[limit:limit2])
            hija.extend(papa[limit:limit2])
            hijo.extend(papa[limit2:])
            hija.extend(mama[limit2:])

        # Si len(genes) no es divisible entre 3 -> la primera y ultima parte serán igual. 
        # la parte de enmedio será 1 número más grande
        else: 
            limit = int(len(self.genes)/3)
            hijo = papa[0:limit]
            hija = mama[0:limit]
            limit2 = limit + limit
            hijo.extend(mama[limit:limit2+1])
            hija.extend(papa[limit:limit2+1])
            hijo.extend(papa[limit2+1:])
            hija.extend(mama[limit2+1:])
         
            
        # En este momento los hijos son listas, no individuos
        hijaObj = Individuo(self.d)
        hijaObj.genes = hija
        hijoObj = Individuo(self.d)
        hijoObj.genes = hijo
        return [hijoObj, hijaObj] # retorna hijos
        
    def mutar(self):
        #Mutacion extrema: Cambia todo el individuo
        self.genes = random.choices([0,1], k= len(self.genes))
            
   
