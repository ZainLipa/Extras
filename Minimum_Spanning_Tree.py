# Program of the Day: Prim's Algorithm (Minimum Spanning Tree)

import heapq

def prim_mst(graph):
    mst = []
    visited = set()
    start_node = list(graph.keys())[0]
    min_heap = [(0, start_node)]

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        if node in visited:
            continue
        visited.add(node)
        mst.append((node, cost))

        for neighbor, edge_cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_cost, neighbor))

    return mst

# Example usage
graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'H': 11, 'C': 8},
    'C': {'B': 8, 'I': 2, 'F': 4, 'D': 7},
    'D': {'C': 7, 'F': 14, 'E': 9},
    'E': {'D': 9, 'F': 10},
    'F': {'E': 10, 'D': 14, 'C': 4, 'G': 2},
    'G': {'F': 2, 'I': 6, 'H': 1},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7}
}

minimum_spanning_tree = prim_mst(graph)
print("Minimum Spanning Tree (Prim's Algorithm):")
for node, cost in minimum_spanning_tree:
    print(f"{node} - {cost}")
