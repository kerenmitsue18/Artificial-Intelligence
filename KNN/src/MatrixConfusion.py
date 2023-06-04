# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: Machine Learning
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Matruiz de confisión

Created on Mon Sep 27 15:09:15 2021

@author: KerenMitsue
"""
import numpy as np 
class MatrixConfusion:
    
    def __init__(self, Yreal, Ypred):
        '''
        

        Parameters
        ----------
        Yreal : List
            DESCRIPTION. Etiquetas real
        Ypred : List
            DESCRIPTION. Etiquetas predicted

        Returns
        -------
        None.

        '''
        self.Yreal = Yreal
        self.Ypred = Ypred
        
    def computeConfusionMatrix(self):
        Yreal = np.array(self.Yreal)
        Ypred = np.array(self.Ypred)
        clases = list(set(Yreal))
        PR = Yreal == clases[0]
        PP = Ypred == clases[0]
        TP = np.sum(PR == PP)
        print(TP)
        #Terminar matriz de confusion 