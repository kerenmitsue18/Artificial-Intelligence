# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Computo evolutivo
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau

Descripción: Búsqueda del mínimo de una función
univariable, usando cualquier método visto

f(x) = sin (e^ (sin (3x)* cos(5x)) )

Created on Wed Aug 11 15:17:57 2021

@author: KerenMitsue
"""

import numpy as np
from matplotlib import pyplot as plt

def fx(x):
    return np.sin( np.exp(np.sin(3 * x) * np.cos(5*x)))
    
def grafica(x, f):
    fig, axs = plt.subplots(1)
    axs.plot(x,f)

'''Encuentra el mínimo de f en el intervalo xmin a xmax'''

def findMinium(xmin, xmax, fun):
    # proponer las soluciones posibles
    x = np.arange(xmin, xmax, 0.001)
    values = fun(x)
    indice = np.argmin(values)
    grafica(x, values)
    return x[indice]
    
    
    '''
    Parameters
    ----------
    xmin : TYPE
        DESCRIPTION.
    xmax : TYPE
        DESCRIPTION.
    f : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''

minimo = -1
maximo = 1
sol = findMinium(minimo,maximo,fx)
print(sol)