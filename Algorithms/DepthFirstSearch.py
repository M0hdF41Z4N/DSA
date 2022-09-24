#   Depth First Search (DFS)

# Working
# Step 1: first select the source vertex and mark the vertex as visited.
# Step 2: pile up (stack) all adjacent edges from the vertex.
# Step 3: once exploration done then repeat from step 1 for vertex on top of the stack.

from collections import defaultdict


class Graph:
    # Constructor
    def __init__(self) -> None:
        self.graph = defaultdict(list) # Allocate infinite list to graph

    # Function to add edge to graph
    def addEdge(self,v,item):
        self.graph[v].append(item)

    # Function used by DFS
    def DFS_util(self,v,visited):
        visited.add(v)
        # To print visited Vertex
        print(v,end="->")
        for neighbhour in self.graph[v]:
            if neighbhour not in visited:
                self.DFS_util(neighbhour,visited)

    # Main DFS traversal function
    def DFS(self,v):
        visited = set()
        self.DFS_util(v,visited)



# Driver Code


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)



g.DFS(1)
