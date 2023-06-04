"""
UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO
UA: INTELIGENCIA ARTIFICIAL
Tema: Algoritos Evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Pruebas del AE del agente viajero
Created on Mon Sep 13 00:52:16 2021
@author: KerenMitsue
"""

from Grafica import Grafica
from FitnessFunction import FitnessFunction
import pandas as pd
from Distancias import Distancias
from AlgoritmoEvolutivo import AlgoritmoEvolutivo

# Pedir al usuario los puntos
tam = int (input("Ingresa numero de ciudades: "))
grafica = Grafica()
points = grafica.generapuntos(tam) #pedir puntos a partir de un plano (x,y)
 

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

ff = FitnessFunction(distancias, ciudades) #Funcion aptitud

ae = AlgoritmoEvolutivo(ff, ciudades,points, 100, 500)
ae.evolve()


