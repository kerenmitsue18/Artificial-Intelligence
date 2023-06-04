# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial 
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
K- means usuarios en Twiter
Created on Mon Oct 18 14:42:25 2021

@author: KerenMitsue

"""

import pandas as pd 
import numpy as np
from showData import ShowData

data = pd.read_csv('../data/analisis.csv')
data.head()
data.describe() #muestra información del dataframe
data.groupby('categoria').size()

show = ShowData()
#show.histogram(data)

x = np.array(data[["op","ex","ag"]])
y = np.array(data['categoria'])
x.shape
#show.plot3D(x, y)

show.plotNK(x)