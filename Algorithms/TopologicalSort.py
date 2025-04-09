import deque from deque

def TopologicalSortBFS(v,edges,adjList):
  indegree = [0] * v
  toposort = [0] * v
  # calculating indegree
  for u,v in edges:
    indegree[u] += 1

  q = new dequeu()
  
  # finding starting point or vertext with zero dependency
  for i in range(v):
    if indegree[i] == 0:
      q.add(i)

  i = 0

  while q:
    node = q.popleft()
    # add to topological sort
    topo[i] = node
    i+=1

    for edge in adjList[node]:
      indegree[edge] -= 1
      # Add vertex with zero dependency to queue
      if indegree[edge] == 0:
        q.add(edge)
        
  return toposort


def TopologicalSortDFS(v,edges,adjList):
  visit = [0] * v
  stack = []
  for i in range(v):
    if visit[i] == 0:
      findTopoSort(i,stack,adjList)

  toposort = stack[::-1]
  return toposort
  

def findTopoSort(node,stack,adjList):
  visit[node] = 1
  for edge in adjList[node]:
    if visit[edge] == 0:
      findTopoSort(edge,i+1,indegree,adjList)
  stack.append(node)
  
