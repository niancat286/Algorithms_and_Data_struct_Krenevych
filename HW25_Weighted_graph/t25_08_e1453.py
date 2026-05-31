from math import inf

edges = []
n = 0


def init(vertices):
    global edges, n
    n = vertices
    edges = []

def addEdge(source, destination, weight):
    edges.append((source, destination, weight))

def findDistance(start):   #белман-форд

    distances = [inf] * (n+1)
    distances[start] = 0

    for _ in range(n-1):
        for u, v, weight in edges:
            if distances[u] != inf:
                new_dist = distances[u] + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    is_relaxed = False

    return distances


if __name__ == "__main__":
    with open("input.txt") as f:
        n_vertices, m_edges = map(int, f.readline().split())
        init(n_vertices)
        for _ in range(m_edges):
            u, v, w = map(int, f.readline().split())
            addEdge(u, v, w)
    distances = findDistance(1)

    result = []
    for i in range(1, n + 1):
        if distances[i] == inf:
            result.append(30000)
        else:
            result.append(distances[i])

    print(*result)