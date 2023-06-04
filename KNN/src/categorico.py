# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 

Created on Wed Oct 13 14:20:29 2021

@author: KerenMitsue
"""

import pandas as pd
import random

# El conjunto de datos no tiene nombre de columnas o variables
data = pd.read_csv("../data/shuttle.csv", header = None)
data.columns = ["Attr" + str(i) for i in list(data.columns)]

Y = data.iloc[:,1] #class
X = data.iloc[:,1:] #Attribute

# Separate data in test
idx = list(range(X.shape[0]))
random.shuffle(idx)


#  Training set (selección pseudo-aleatoria)
#  66% para entrenamiento
Xtr = pd.DataFrame(columns=X.columns)
Ytr = []
for i in range(int(len(idx)*.66)):
    Xtr = Xtr.append(X.iloc[idx[i], :])
    Ytr.append(Y[idx[i]])

#  Test set
Xtest = pd.DataFrame(columns=X.columns)
Ytest = []
for i in range(int(len(idx)*.66), len(idx)):
    Xtest = Xtest.append(X.iloc[idx[i], :])
    Ytest.append(Y[idx[i]])
    
Xtr.reset_index(inplace = True, drop=True)
