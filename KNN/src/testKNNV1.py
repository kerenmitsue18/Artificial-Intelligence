# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: Machine Learning
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: Prueba KNN

Created on Mon Sep 27 15:09:15 2021

@author: KerenMitsue
"""
import numpy as np
import pandas as pd
from KNNV1 import KNNV1
import random
from MatrixConfusion import MatrixConfusion
################
accs = []
datos = pd.read_csv("../data/iris.csv")
X = datos.iloc[:, 0:-1] # Atributos
Y = datos.iloc[:, -1]   # Etiquetas
# Revolver los indices
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

clf = KNNV1()
clf.fit(Xtr, Ytr, K=3, distance="Euclidean")
ypred = clf.predict(Xtest)
# Medir que tan bien predice las etiquetas
suma = np.sum(np.array(Ytest) == np.array(ypred))
accuracy = suma/len(Ytest)
print("Accuracy = {:.2f}".format(accuracy))
#accs.append(accuracy)
    ##########
#print("Acc: "+str(np.mean(accs)))
#print("STD: "+ str(np.std(accs)))
    
# Calcular el promedio y desviación estándar
# de la accuracy del clasificador K-NN para
# 10 ejecuciones del algoritmo

#print(clf.predict(np.array([1.0,2.5,4.5,8])))
#Matriz de confusión 
mc = MatrixConfusion(Ytest,ypred)
mc.computeConfusionMatrix()

