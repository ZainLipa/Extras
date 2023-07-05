# Program of the Day: Dijkstra's Algorithm

import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Example usage
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)
print("Shortest distances from vertex", start_vertex + ":")
for vertex, distance in distances.items():
    print("To vertex", vertex + ":", distance)

