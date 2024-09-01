# Bellman Ford
# 	Finds shortest path 
# 	Works on both directed and undirected graph, weighted graph
# 	Dynamic Programming
# 	Drawback - doesn't work for negative cycle graph (This cannot be solved at all)
#   Youtube - https://www.youtube.com/watch?v=FtN3BYH2Zes
#   Geeksforgeeks - https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def addEdge(self, u,v, w):
        self.graph.append([u,v,w])

    def BellmanFord(self, src):
        #1. Initialize the array for each vertex with infinity as the value
        dist = [float("Inf")]*self.V
        dist[src] = 0
        #2. Relax the value of vertex V-1 times
        for i in range(self.V - 1):
            for j in range(len(self.graph)):
                u,v,w = self.graph[j]
                if(dist[u] != float("Inf") and dist[u] + w < dist[v]):
                    dist[v] = dist[u] + w
                
        #3. Perform relaxation once more just to confirm if there are no negative cycles
        for j in range(len(self.graph)):
            u,v,w = self.graph[j]
            if(dist[u] != float("Inf") and dist[u] + w < dist[v]):
                print("Cycle with negative edges present")
                return
        
        print(dist)

if __name__=="__main__":
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    g.BellmanFord(0)

