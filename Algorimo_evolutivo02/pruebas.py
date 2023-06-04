#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Pruebas preliminares


Created on Mon Sep 13 00:26:48 2021

@author: KerenMitsue
"""
'''
from AlgoritmoEvolutivo import AlgoritmoEvolutivo
ae = AlgoritmoEvolutivo("asdrubal lopez chau", 100, 700)
ae.evolve(400)
Mejora de la arquitectura del algoritmo evolutivo
'''
from FitnessFunction import FitnessFunction
from AlgoritmoEvolutivo import AlgoritmoEvolutivo

ff = FitnessFunction("hola mundo")
ae = AlgoritmoEvolutivo(ff, 100, 600)# Al construir un objeto AE 
                    # se le pasa la función de aptitud a usar.
ae.evolve(500)