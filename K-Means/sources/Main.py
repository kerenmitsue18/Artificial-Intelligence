# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: K-Means
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Prube K-means
Created on Wed Oct 20 14:56:38 2021

@author: KerenMitsue
"""

import pandas as pd
import numpy as np
from MyKmeans import MyKmeans
data = pd.read_csv("../data/cluster.csv", header=None)  #Archivo
columns = ["a" +  str(i) for i in range(data.shape[1])] #Nombre de columnas
data.columns = columns


#Normalizar datos
maximos = np.max(data.abs(), axis=0)
maximos = list(maximos)
i=0
values = []
for maxi in maximos:
    a = data.iloc[0:1000,i]/maxi
    values.append(a)
    i+=1
    
#Generar otro DataFrame
dataNorm = pd.DataFrame(columns = data.columns) #Generar dataFrame
dataNorm = pd.concat(values, axis=1) #Concatenar columnas
dataNorm.columns = columns #Editar columnas

kmeans = MyKmeans()
kmeans.fit(dataNorm, K=6)
#kmeans.predict(dataNorm[500:1000])
