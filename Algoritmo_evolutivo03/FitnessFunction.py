"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Algoritmos evolutivos
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
    Encontrar el minimo de la siguiente función:
        f(x) = 10d + sumatoria de i = 1 hasta d ( xi^2 - 10cos(2*pi*xi))

Función objetivo del problema
Created on Fri Sep 03 14:11:36 2021
@author: KerenMitsue
"""

from Individuo import Individuo
import numpy as np

class FitnessFunction:
    
    def fitness(self, individuo):
        suma = 0
        xi = individuo.getPhenotype() # Obtener fenotipo
        fx = 10 * len(xi) # Primera parte del algoritmo
        for i in range (len(xi)):
            suma += np.square(xi[i]) - 10 * np.cos( 2 * np.pi * xi[i]) # sumatorias de 1 hasta número de variables
        fx = fx + suma # Función
        return fx # Retorna la función en negativo