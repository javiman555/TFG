import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

class K_Means:
    def __init__(self, k, precision = 0.0001):
        self.k = k
        self.precision = precision
        self.dataNames = []
        self.boxes = {}
    
    def fitDefault(self,listComplexWave):
        self.boxes = self.fitDefaultProcess(listComplexWave)
        return self.boxes
    
    def fitDefaultProcess(self,listComplexWave):
        
		#initialize the centroids, the first distinct 'k' elements in the dataset will be our initial centroids 
        centroids = self.initializeClustersFirstElements(listComplexWave,self.k)

		#begin iterations
        while True:
            boxes = {}
            for i in range(self.k):
                boxes[i] = []

			#find the distance between the point and cluster; choose the nearest centroid
            for wave in listComplexWave:
                
                distances = self.calculateDistancesDefault(wave,centroids)

                classification = distances.index(min(distances))
                boxes[classification].append(wave)
            previousCentroids = dict(centroids)

			#average the cluster datapoints to re-calculate the centroids
            isOptimal =self.averageCluster(previousCentroids,centroids,boxes)
			#break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
            if isOptimal:
                return boxes
        
        
	#initialize the centroids, the first distinct 'k' elements in the dataset will be our initial centroids 
    def initializeClustersFirstElements(self, listComplexWave,k):
        output = {}
        i = 0
        j = 0
        while i < k :
            if j >= len(listComplexWave):
                #Case we run out of elements asignating centroids
                nextCentroid = max(output.values()) + 1
            else :
                nextCentroid = listComplexWave[j]
            
            j = j + 1
            if (not nextCentroid in output.values()):
                output[i] =nextCentroid
                i = i + 1
        for i in range(k):
            output[i] = listComplexWave[i].y
        return output
            
    #average the cluster datapoints to re-calculate the centroids and returs if we finish the proccess
    def averageCluster(self,previousCentroids,centroids,boxes):
        for classification in boxes:
                
            centroids[classification]=[] 
            for i in range(len(boxes[classification])):
                centroids[classification].append(boxes[classification][i].y)
            
            if not centroids[classification]:
                #Error empty centroid
                centroids[classification] = [[0]*len(previousCentroids[0])]
            centroids[classification] = np.average(centroids[classification], axis = 0)


        for centroid in centroids:

            original_centroid = previousCentroids[centroid]
            curr = centroids[centroid]
            change = self.change(curr,original_centroid)
                
            if change > self.precision:
                return False
        return True
    
    #Catches to elements of the original_centoroid that are 0
    def change(self,curr,original_centroid):
        change = 0
        for i in range(len(original_centroid)):
            if original_centroid[i] != 0:
                change = change + (abs(((curr[i] - original_centroid[i])/original_centroid[i] )* 100.0))
        return change
    
    #Uses the norm of n dimensions to get distance
    def calculateDistancesDefault(self, wave, centroids):
        output = []
        for centroid in centroids:
            distance = []
            for i in range(len(wave.y)):
                distance.append(wave.y[i] - centroids[centroid][i])
                
            output.append(np.linalg.norm(distance))
        return output

    def paintAll(self,nrows,ncols):
        for i in self.boxes:
            print("---------- Box "+str(i)+" ----------")
            self.paintBox(self.boxes[i],1,nrows,ncols,i)
        plt.show()
                
    def paintWave(self,y):
        sr = len(y)
        # sampling interval
        ts = 1.0/sr
        x = np.arange(0,1,ts)
        if len(x) != len(y):
            x = np.delete(x,0)
            
        
        plt.plot(x,y, 'k')
        
        
        
        
    def paintBox(self,box,ymax,nrows,ncols,pos):
        
        label=""
        plt.subplot(nrows, ncols, pos+1)
        plt.title('Data of Box - '+ str(pos))
        plt.ylim(0,ymax)
        for i in range(len(box)):
            print(box[i].dataName)
            self.paintWave(box[i].y)
            label = label + " " + (box[i].dataName) + " "
        #ax[pos//nrows,pos%ncols].set_title('Data - '+label)
        #ax[pos//nrows,pos%ncols].set_title('Data of Box - '+str(pos))
        
        
        