# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 

Created on Wed Sep 22 15:42:49 2021

@author: KerenMitsue
"""


import pandas as pd


data = pd.read_csv('../data/iris.csv')
len(data) # longitud de filas
data.shape # Dimensiones (renglones, columnas)
data.shape[0] # renglones
data.shape[1] # columnas
data.columns # Nombre de las columnas
list(data.columns) # Nombre de columnas
data.dtypes # Tipo de cada una de las columnas
data.values #Convierte datos a arreglo numpy
data.iloc[0:10, :] #Acceso por indice (renglones, columna)
data.iloc[:,-1] #Acceso a la ultima columna (sin etiquetas)
data.iloc[:,0:-1] #Acceso a los atributos sin la ultima etiqueta
data.iloc[:,-1] #Etiquetas 

set(data.iloc[:,-1]) # Realiza un conjunto -> identificacion de datos en el DataFrame
list(set(data.iloc[:,-1]))
