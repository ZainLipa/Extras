# Program of the Day: Floyd-Warshall Algorithm

INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    distances = [[INF] * n for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u == v:
                distances[u][v] = 0
            elif v in graph[u]:
                distances[u][v] = graph[u][v]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

# Example usage
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'B': 4, 'C': 2}
}

all_distances = floyd_warshall(graph)
print("All-pairs shortest distances:")
for i in range(len(all_distances)):
    for j in range(len(all_distances[i])):
        if all_distances[i][j] == INF:
            print("INF", end="\t")
        else:
            print(all_distances[i][j], end="\t")
    print()
