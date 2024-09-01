# Djikstra's Algorithm
# 	Optimization problem to find the shortest distance from source to dest in a graph
# 	Greedy Algo
# 	Complexity - O(|V|*|V|) - this is for complete graph
# 	Works on non directed graph
# 	may work or may not work for negative edges
import heapq

class Node:
    def __init__(self,V, distance):
        self.V = v
        self.distance = distance

    def __lt__(self, other):
        return self.distance<other.distance

def DijkstrasAlgorithm(V, adj, S):
    visited = [False]*V
    map = {}
    q = []

    map[S] = Node(S,0)
    heapq.heappush(q, Node(S, 0))

    while(q):
        n = heapq.heappop()
        v = n.V
        distance = n.distance
        visited[n] = True

        adjList = adj[v]
        for adjLink in adjList:
            if(not visited[adjLink[0]]):
                if adjLink[0] not in map:
                    map[adjLink[0]] = Node(v, distance+adjLink[1])
                else:
                    sn = map[adjLink[0]]
                    if distance+adjLink[1] < sn.distance:
                        sn.v = v
                        sn.distance = distance + adjLink[1]
                        
                heapq.heappush(q, Node(adjLink[0], distance+adjLink[1]))

        result = [0]*V
        for i in range(V):
            result[i] = map[i].distance
        return result




if __name__ == "__main__":
    V = 6
    E = 5
    u = [0, 0, 1, 2, 4]
    v = [3, 5, 4, 5, 5]
    w = [9, 4, 4, 10, 3]

    adj = [[] for _ in range(V)]

    for i in range(E):
        edge1 = [u[i], w[i]]
        adj[v[i]].append(edge1)

        edge2 = [v[i], w[i]]
        adj[u[i]].append(edge2)

    S = 1
    result = DijkstrasAlgorithm(V, adj, S)
    print(result)



