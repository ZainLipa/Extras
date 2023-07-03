# Program of the Day: Prim's Algorithm for Minimum Spanning Tree

import heapq

def prim(graph):
    # Initialize an empty minimum spanning tree
    mst = []

    # Select the starting vertex
    start_vertex = list(graph.keys())[0]
    visited = set([start_vertex])

    # Create a priority queue to store edges
    edges = []
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(edges, (weight, start_vertex, neighbor))

    # Run Prim's algorithm until all vertices are visited
    while edges:
        weight, u, v = heapq.heappop(edges)

        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            # Add new edges to the priority queue
            for neighbor, weight in graph[v]:
                heapq.heappush(edges, (weight, v, neighbor))

    return mst

# Example usage
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('A', 6), ('B', 8), ('C', 1), ('E', 4)],
    'E': [('C', 5), ('D', 4)]
}

minimum_spanning_tree = prim(graph)
for edge in minimum_spanning_tree:
    print(edge)

