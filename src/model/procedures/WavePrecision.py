import src.model.objects.graph.ClosenessGraph as cg
import src.model.modules.Wavelete as Wavelete
import src.model.modules.Fourier as Fourier
import src.model.objects.k_means.K_MeansVariation as K_MeansVariation


class WavePrecision:
    
    def __init__(self, realWaveList,flag=1):
        self.realWaveList = realWaveList
        self.realGraph = self.initializeData(realWaveList,flag)
    
    #Gives a graph with kmeans loop data
    def initializeData(self,listWave,flag):
        kmeans = K_MeansVariation.K_MeansVariation(0)
        closenessGraph = cg.ClosenessGraph()
        if flag == 1:
            closenessGraph.distanceCloseness(listWave,kmeans.fitDefault,kmeans)
        elif flag ==2:
            closenessGraph.distanceCloseness(listWave,kmeans.fitByCourse,kmeans)
        elif flag ==3:
            closenessGraph.distanceCloseness(listWave,kmeans.fitByCourseValue,kmeans)

        return closenessGraph
    
    #Gives how similar the aproxGraph is to the realGraph
    def compareData(self,aproxWaveList,flag=1):
        
        aproxGraph = self.initializeData(aproxWaveList,flag)
        #Calibrate weight to go back to k-means coincidence
        self.realGraph.calibrateWeightMax()
        aproxGraph.calibrateWeightMax()
        
        realEdges = self.realGraph.edges(data=True)
        aproxEdges = aproxGraph.edges(data=True)
                
        realEdgeskeys = set(self.realGraph.edges())
        aproxEdgeskeys = set(aproxGraph.edges())
        
        allEdgeskeys = list(realEdgeskeys.union(aproxEdgeskeys))
        
        aproxEdgesWeight = []
        realEdgesWeight =[]
        error = 0
        total = 0
        
        for edge in allEdgeskeys:
            realWeight = self.realGraph.get_edge_data(edge[0],edge[1], default={'weight':0})
            realEdgesWeight.append(realWeight['weight'])
            aproxWeight = aproxGraph.get_edge_data(edge[0],edge[1], default={'weight':0})
            aproxEdgesWeight.append(aproxWeight['weight'])
            total = total + abs(realWeight['weight'])
            #total = total + self.realGraph.maxCloseness
            error = error + 1/2*abs(realWeight['weight']-aproxWeight['weight'])
        
        percentage = (1 - error/total)*100
        #RecalibrateWeightMax to go back to the pseudo distance
        aproxGraph.calibrateWeightMax()
        self.realGraph.calibrateWeightMax()
        
        return percentage
    
    def compareWavelete(self):
        wavelete = Wavelete.Wavelete()
        fourier = Fourier.Fourier()
        aproxWaveList = []
        for realWave in self.realWaveList:
            aproxWave = realWave#100
            #aproxWave = fourier.DFT(realWave)#-6 / 85.579
            aproxWave = wavelete.simplificationComplexWave(aproxWave)#96.36 / 99.8 / 94.35
            #aproxWave = wavelete.simplificationComplexWave(aproxWave)#83.13 /x/
            #aproxWave = wavelete.simplificationComplexWave(aproxWave)#79.28 /x/ 76
            #aproxWave = wavelete.simplificationComplexWave(aproxWave)#66.85 / 94.292 / 55.72
            aproxWaveList.append(aproxWave)
        return self.compareData(aproxWaveList)
    
    
    