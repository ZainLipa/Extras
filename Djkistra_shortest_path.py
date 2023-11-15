# Program of the Day: Dijkstra's Algorithm (Shortest Path)
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 3, 'D': 2},
    'B': {'A': 3, 'D': 5, 'E': 2},
    'C': {'E': 1},
    'D': {'A': 2, 'B': 5, 'E': 4},
    'E': {'B': 2, 'C': 1, 'D': 4}
}
start_node = 'A'

shortest_distances = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, "to all other nodes:")
for node, distance in shortest_distances.items():
    print(node, ":", distance)
