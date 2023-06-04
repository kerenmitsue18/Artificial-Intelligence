# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Prueba del funcionamiento del algoritmo Evolutivo
PRUEBA DE FUNCIONAMIENTO
Created on Mon Aug 23 14:49:13 2021

@author: KerenMitsue
"""

from Individuo import Individuo
from FitnessFunction import FitnessFunction
from Poblacion import Poblacion
from Seleccion import Seleccion 


ff = FitnessFunction()
'''
i = Individuo()
i.inicializa()

print(i)
print(ff.fitness(i))
'''

N = 5 # Tamaño de poblacion
pob = Poblacion(N)
print(pob)
print('Best:' , str(pob.best()))

sel = Seleccion()
padres = sel.seleccionaPadres(pob, 2)
print(padres)
papa = pob.poblacion[padres[0]]
mama = pob.poblacion[padres[1]]
print('Mama: ', mama)
print('Papa', papa)
hijo, hija = mama.cruza(papa)

hijo.mutar()
print(hijo)
