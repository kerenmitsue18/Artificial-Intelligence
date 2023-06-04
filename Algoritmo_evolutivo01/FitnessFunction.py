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

FUNCION DE APTITUD
Created on Mon Aug 23 14:45:54 2021

@author: KerenMitsue
"""
from Individuo import Individuo

class FitnessFunction:
    
    def fitness(self, individuo):
        x, y = individuo.getPhenotype()
        return -((x-1.)**2 + (y+3)**2)