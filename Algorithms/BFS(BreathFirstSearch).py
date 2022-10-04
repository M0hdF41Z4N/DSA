# Breath first Search (BFS)

# Working of BFS
# Step 1: Select the vertex and mark it visited
# Step 2: then add all adjacent vertex into the Queue and mark them visited
# Step 3: Repeat Step 1 from the vertex in Queue  

from collections import defaultdict

class Graph:
    # Constructor
    def __init__(self):
        self.graph = defaultdict(list)

    # Function to add edge to graph
    def addEdge(self,v,item):
        self.graph[v].append(item)

    # Function of BFS
    def BFS(self,v):
        visited = set()
        visited.add(v) # add the first vertex
        Queue = [v] #   add the vertex in queue
        while Queue:
            v = Queue.pop(0) # pop the vertex from queue
            print(v,end=" -> ")
            for neigbhour in self.graph[v]:
                if neigbhour not in visited:
                    visited.add(neigbhour)
                    Queue.append(neigbhour)
                    
                    
             

                    



# Driver Code


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)



g.BFS(2)