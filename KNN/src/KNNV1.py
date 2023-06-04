# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: Inteligencia Artificial
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Clasificacion con K vecinos más cercanos
K-Nearest- Neighbors Versión 1

Created on Mon Sep 27 15:01:56 2021

@author: KerenMitsue
"""
import pandas as pd
import numpy as np
from collections import Counter
import re

class KNNV1:
    
    def fit(self, X, Y,K=3,distance = 'Euclidean'):
        '''
        Entrena al clasificador

        Parameters
        ----------
        X : DataFrame
            Valores de los atributos
        Y : Series
            Etiquetas.
        K : int, optional
            Número de vecinos más cercanos. The default is 3.
        distance : str, optional
            distancia a utilizar. The default is 'Euclidean'.

        Returns
        -------
        None.

        '''
        self.K = K
        self.distance = distance
        self.X = X
        self.Y = Y
        

    
    def distances(self, xi):
        '''
        Calcula todas las distancias desde xi hasta cada elemento de
        Self.X

        Parameters
        ----------
        xi : array numpy 
            instancia, muetra, objeto

        Returns
        -------
        distancias : List
        Lista que contiene todas las distancias desde x1 hasta 
        cada elemento de self.x
        '''
        Xdatos = self.X.values
        distance = []
        
        
        for j in range(len(Xdatos)):
            xj = Xdatos[j]
            dxi_xj = np.sqrt(np.sum(np.power(xi - xj, 2)))
            distance.append(dxi_xj)
   
        return distance
            
    
    def getKminimunDistances(self,distancias):
        '''
        Obtiene los objetos o instancias con menor distancia

        Parameters
        ----------
        distancias : list
            Distancias desde x1 hasta cada elemento del 
            self.X
        Returns
        -------
        idxs : list
            Indices de x1 con menor distancia

        '''
        idxs = []
        for k in range(self.K):
            idx = np.argmin(distancias)
            idxs.append(idx)
            #Error, no eliminar porque los indices cambian
            #distancias.remove(distancias[idx])
            #Correción
            distancias[idx] = np.max(distancias)
        return idxs
            
  
    
    def claseMasFrecuente(self, idx):
        '''
        TODO: Implementar desempate

        Parameters
        ----------
        idx : List
            DESCRIPTION.Indice de los vecinos más cercanos

        Returns
        -------
        TYPE str
            DESCRIPTION.Clase más frecuente

        '''
        KClases = [self.Y[i] for i in idx]
        conjunto = list(set(KClases))
        
        frecuencia= [KClases.count(i) for i in conjunto]
        idx = np.argmax(frecuencia)
        return conjunto[idx]
    
    def predict(self, X):
        '''
        Realiza la predicción de etiquetas con KNN

        Parameters
        ----------
        X : DataFrame
            Atributos

        Returns
        -------
        list: lista de prediciones

        '''
        ypred = []
        if type(X) is pd.DataFrame:
            X = X.values
            
            for xi in X:
            
                distancias = self.distances(xi)
                # Determinar las self.K distancias más pequeñas (indices)
                idx = self.getKminimunDistances(distancias)
                # Calcular la etiqueta más frecuente
                # frecuency = self.frecuencyTable(self.getLabel(id))
                #label = Counter(self.getLabel(id)).most_common(1)
                #ypred.append(self.strLabel(label))
                ypred.append(self.claseMasFrecuente(idx))
        elif type(X) is np.ndarray:
            distancias = self.distances(X)
            # Determinar las self.K distancias más pequeñas (indices)
            idx = self.getKminimunDistances(distancias)
            ypred.append(self.claseMasFrecuente(idx))
            
        return ypred

    
            
            