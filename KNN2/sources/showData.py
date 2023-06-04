# -*- coding: utf-8 -*-
"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: REDES NEURONALES
Tema: 
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 

Created on Mon Oct 18 14:51:25 2021

@author: KerenMitsue
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.cluster import KMeans

class ShowData:
    
    def histogram(self, data):
        sb.pairplot(data.dropna(), hue='categoria',size=4,vars=["op","ex","ag"],kind='scatter')
        plt.show()
        
    def plot3D(self,x,y):
        fig = plt.figure()
        ax = Axes3D(fig)
        colours = ['blue','red','blue','cyan','yellow','orange','black','pink','brown','purple']
        assing = []
        for c in y:
            assing.append(colours[c])
        ax.scatter(x[:,0],x[:,1],x[:,2], c=assing, s=60)
    
    def plotNK(self,x):
        Nc = range(1,20)
        Kmeans= [KMeans(n_clusters=i) for i in Nc]
        score = [Kmeans[i].fit(x).score(x) for i in range(len(Kmeans))]
        score
        plt.plot(Nc,score)
        plt.xlabel('Number of clusters')
        plt.ylabel('Score')
        plt.title('Elbow Curve')
        plt.show()