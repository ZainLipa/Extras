# Program of the Day: Depth-First Search (DFS)

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start)
    visited.add(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_vertex = 'A'
print("DFS traversal:")
dfs(graph, start_vertex)
