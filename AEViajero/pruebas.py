"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Pruebas preliminares para el problema TSP

Created on Mon Sep 13 00:52:16 2021

@author: KerenMitsue
"""
from Grafica import Grafica
from Individuo import Individuo
from FitnessFunction import FitnessFunction
from Seleccion import Seleccion
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from Distancias import Distancias
from AlgoritmoEvolutivo import AlgoritmoEvolutivo

# Pedir al usuario los puntos
tam = int (input("Ingresa numero de ciudades: "))
grafica = Grafica()
points = grafica.generapuntos(tam)
 

# Calcular las distancias entre los puntos
d = Distancias();
distancias = d.calculaDistancia(points)

# Guardarlo en un archivo CSV 
datos = pd.DataFrame(distancias)
datos.to_csv("distancias.csv", index = False)

#Realizar lista de ciudades 
ciudades = []
for i in range (len(points)):
    cad = "C{:1}".format(i+1)
    ciudades.append(cad)
"""
distancias = [[0],
              [12],
              [34.5, 6.1],
              [9.0, 23.0, 5.8]              
              ]
ciudades = ['A', 'B', 'C', 'D']
"""
ff = FitnessFunction(distancias, ciudades)

ae = AlgoritmoEvolutivo(ff, ciudades,points, 10)
ae.evolve(10)


