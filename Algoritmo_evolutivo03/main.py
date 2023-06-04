# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
Prueba del algoritmo completo

Created on Wed Sep 01 15:41:58 2021

@author: KerenMitsue
"""


from AlgoritmoEvolutivo import AlgoritmoEvolutivo #importar clase AlgoritmoEvolutivo

# Ingresar datos
Tam_Pob = int (input('Ingrese tamaño de poblacion: '))
generaciones = int (input('Ingrese # de generaciones: '))
d = int(input('Ingrese # Variables: '))

print("\n")

# Realizar algoritmo evolutivo
ae = AlgoritmoEvolutivo(d, Tam_Pob,generaciones )
ae.evolve(generaciones)
