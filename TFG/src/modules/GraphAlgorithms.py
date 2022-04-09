import sys



class GraphAlgorithms:

    def __init__(self):
        pass


    
    def centralidadv1(grafo):
        cent = {}
        for v in grafo: cent[v] = 0
        for v in grafo:
            for w in grafo:
                if v == w: continue
                # con el algoritmo que corresponda al grafo
                distancia, padre = camino_minimo(grafo, v, w)
                # salteamos si no hay camino de v a w
                if padre[w] is None: continue
                actual = padre[w]
                # le sumamos 1 a la centralidad de todos los vertices que se encuentren en
                # el medio del camino
                while actual != v:
                    cent[actual] += 1
                    actual = padre[actual]
        return cent
    
    def pSol(self,grafo, dist):
        print("Distance of vertex from source")
        for node in range(grafo.V):
            print(node, "t", dist[node])
 

    def minDistance(self,grafo, dist, sptSet):
 

        min = sys.maxsize
 

        for v in range(grafo.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 

    def dijk(self,grafo, source):
 
        dist = [sys.maxsize] * grafo.V
        dist[source] = 0
        sptSet = [False] * grafo.V
 
        for cout in range(grafo.V):
 
            u = self.minDistance(dist, sptSet)
 
            sptSet[u] = True
 

            for v in range(grafo.V):
                if grafo.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + grafo.graph[u][v]:
                    dist[v] = dist[u] + grafo.graph[u][v]
 
        self.pSol(dist)