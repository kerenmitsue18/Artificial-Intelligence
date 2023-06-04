# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Calculas las distancias de los puntos datos 

Created on Tue Sep 14 22:12:42 2021

@author: KerenMitsue
"""
import numpy as np
class Distancias: 
    
    def calculaDistancia(self, points):
        distancias = []
        disCiudad = []
        for i in range (len (points)):
            for j in range (len(points)):
                cityA = points[i]
                cityB = points[j]
                if (j<i):   
                    distancia = np.sqrt(  np.square(cityA[0] - cityB[0] ) + np.square( cityA[1] - cityB[1]))
                    disCiudad.append(distancia) 
                elif (i==j and i==0):
                    distancias.append([0.0])
                else:
                     pass
            if len(disCiudad) != 0: 
                distancias.append(disCiudad)     
            disCiudad = []
        return distancias
                