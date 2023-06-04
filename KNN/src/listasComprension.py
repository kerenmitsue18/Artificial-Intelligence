# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Listas por comprensión 

Created on Wed Oct  6 14:39:14 2021

@author: KerenMitsue
"""

pares = []
for i in range(10): 
        if i%2 ==0:
            pares.append(i)
            
pares  = [ i for i in range(10)]
pares = [i for i in range(10) if i%2==0]

#Ejemplo: frutas que no tengan una letra
frutas = ["mango", "kiwi", "sandia", "fresa", "piña", "coco"]
#Frutas sin "a"
frutasSinA = [f for f in frutas if "a" not in f]


#crea un coctel de frutas que tengan dos vocales repetidas
coctel = [f for f in frutas if f.count('o')>1 
             or f.count('a')>1 or f.count('e')>1 or f.count('i')>1 or f.count('u')>1]
