from collections import deque

def kahn_topological_sort(graph):
    in_degree = {u: 0 for u in graph}
    
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    topological_order = []
    
    while queue:
        u = queue.popleft()
        topological_order.append(u)
        
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    if len(topological_order) != len(graph):
        raise ValueError("Graph has at least one cycle!")
    
    return topological_order
