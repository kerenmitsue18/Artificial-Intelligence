# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: Machine Lerarnign 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Graficar los datos de un conjunto etiquetado

Created on Mon Sep 27 14:08:38 2021

@author: KerenMitsue
"""

import pandas as pd
from matplotlib import pyplot as plt 


#Leer los datos 
datos = pd.read_csv('../data/iris.csv')
# Seleccionamos las dos primeras dimensiones
X = datos.iloc[:,0:2]
# Seleccionamos las clases
Y = datos.iloc[:,-1]


class GraficaClases:
    
    def plot2D(self, X,Y):
        '''
        Grafica las clases en un conjunto de etiquetado
        con dos atributos
        Parameters
        ----------
        x : DataFrame
            Contiene los atributos
        y : Serie de pandas
            Contiene las etiquetas o clases

        Returns
        -------
        None.

        '''
        
        colores = ['or', 'sg', 'hb', '*y']
        clases = list(set(Y))
        fig, axs = plt.subplots(1)
        clasesName = []
        for i in range (len(clases)):
            x = X.loc[Y == clases[i]].iloc[:,0]
            y = X.loc[ Y == clases[i]].iloc[:,1]
            axs.plot(x,y,colores[i])
            clasesName.append(clases[i])
            
        nombreAtts = (X.columns)
        axs.set_xlabel(nombreAtts[0])
        axs.set_ylabel(nombreAtts[1])
        axs.legend(clasesName)

gc = GraficaClases()
gc.plot2D(X, Y)
 