# Program of the Day: Bellman-Ford Algorithm (Shortest Path)

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                return "Graph contains negative-weight cycle"

    return distances

# Example usage
graph = {
    'A': {'B': -1, 'C': 4},
    'B': {'C': 3, 'D': 2, 'E': 2},
    'C': {},
    'D': {'B': 1, 'C': 5},
    'E': {'D': -3}
}
start_node = 'A'

shortest_distances = bellman_ford(graph, start_node)
print("Shortest distances from node", start_node, "to all other nodes:")
for node, distance in shortest_distances.items():
    print(node, ":", distance)
