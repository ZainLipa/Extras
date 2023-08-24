# Program of the Day: Traveling Salesman Problem (TSP) - Brute Force

import itertools

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Return to starting city
    return total_distance

def brute_force_tsp(graph):
    cities = list(graph.keys())
    shortest_path = None
    min_distance = float('inf')

    for path in itertools.permutations(cities):
        distance = calculate_total_distance(path, graph)
        if distance < min_distance:
            min_distance = distance
            shortest_path = path

    return shortest_path, min_distance

# Example usage
graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

shortest_path, min_distance = brute_force_tsp(graph)
print("Shortest Path:", shortest_path)
print("Minimum Distance:", min_distance)
