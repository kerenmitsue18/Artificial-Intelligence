# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
Prueba del algoritmo completo
Created on Wed Aug 25 15:41:58 2021

@author: KerenMitsue
"""


from AlgoritmoEvolutivo import AlgoritmoEvolutivo
Tam_Pob = int (input('Ingrese tamaño de poblacion: '))
generaciones = int (input('Ingrese # de generaciones: '))
ae = AlgoritmoEvolutivo(Tam_Pob,generaciones )
ae.evolve(generaciones)