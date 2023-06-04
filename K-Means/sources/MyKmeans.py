"""UNIVERSIDAD AUTÓNOMA DEL ESTADO DE MÉXICO
CU UAEM ZUMPANGO 
UA: Inteligencia Artificial
Tema: K-Means
Alumno: Keren Mitsue Ramírez Vergara
Profesor: Dr. Asdrúbal López Chau
Descripción: 
Implementacion 
Created on Wed Oct 20 14:56:38 2021

@author: KerenMitsue
"""

import numpy as np

class MyKmeans:
    
    def __init__(self):
        pass
    
    def chooseCentroids(self):
        '''
        Choose K centroids of self.X

        Returns
        -------
        None.

        '''
        indices = np.random.randint(0, len(self.X), self.K)
        centroids = [ self.X.iloc[i,:] for i in indices ]
        self.centroids = np.array(centroids)
        
    def fit(self,X,K=2):
        '''
        
        Parameters
        ----------
        X : DataFrame
            DataFrame of values
        K : int
            num centroids

        Returns
        -------
        None.

        '''
        self.K = K
        self.X = X
        self.chooseCentroids()
        for i in range(10):
            print('\nIterations:', (i+1), "\n")
            print("The centroids are\n", self.centroids)
            distances = self.distance() #distances 
            self.assignCentroid(distances) #assign Centroids
            self.update() # update centroids
            
           
    
    def predict(self,X):
        '''
        Predict the assign the centroides of X

        Parameters
        ----------
        X : Data Frame
            Values to predict

        Returns
        -------
        None.

        '''
        self.X = X
        distances = self.distance()
        self.assignCentroid(distances)
        print("The predict is: ", self.assign)
    
    def computeDistance(self, ci):
        '''
        Calculate distance of centroids and all values

        Parameters
        ----------
        ci : Series
            Centroids ci

        Returns
        -------
        list all distances
        '''
        distances = []
        xdatos = self.X.values
        for i in xdatos:
                distance = np.sqrt(np.sum(np.square(i -ci))) #distance euclidian
                distances.append(distance)
        #print(distances)
        return distances
        
        
    def assignCentroid(self, distances):
        '''
        Assign each self.X the centroid nearest

        Parameters
        ----------
        distances : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        self.assign = np.argmin(distances, axis=0)       
        #print("\nThe assign is \n", self.assign)
    
        
    def distance(self):
        '''
        Calculate all distances of centroids

        Returns
        -------
        array
            distances from centroids to all values

        '''
        distances = []
        for ci in self.centroids:
            d = self.computeDistance(ci)
            distances.append(d)
            #print("The distances of centroid: ", ci,"are\n", d )
        return np.array(distances)
        
    def setCentroids(self, idx):
        '''
        Calculate set of centroid

        Parameters
        ----------
        idx : int
            index of centroid

        Returns
        -------
        values : array
            values belonging to a centroid

        '''
        values = []
        for s in range(len(self.assign)):
            value = self.X.values[s]
            if (self.assign[s] == idx and (np.not_equal(value, self.centroids[idx]).all) ):
                values.append(value)
            else:
                pass
        return values
    
    def update(self):
        '''
        Update all centroides

        Returns
        -------
        None.

        '''
        for i in range(len(self.centroids)):
            ci = self.updateCentroid(self.centroids[i], i)
            self.centroids[i] = ci
        #print("The new centroids\n", self.centroids)
    
    def updateCentroid(self, ci, i):
        '''
        calculate mean of each centroid

        Parameters
        ----------
        ci : list
            Value of centroid
        i : num
            index of this centroid

        Returns
        -------
        ci : array
            updated centroid

        '''
        for c in range(len(ci)):
            values = self.setCentroids(i)
            #print("Set of centroids ", i, "is \n", values)
            sumas = np.sum(values, axis=0)
            ci[c] = sumas[c]/np.abs(len(values))
        return ci
