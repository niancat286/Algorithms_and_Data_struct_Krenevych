

class Graph:

    def __init__(self, n):
        self.n = n
        self.vertices = [[] for _ in range (n+1)]

    def add_edge(self, v1, v2, id):
        self.vertices[v1].append((v2, id))
        self.vertices[v2].append((v1, id))

    def is_connected(self, banned_vertices):

        visited = [False] * (self.n + 1)

        stack = [1]
        visited[1] = True
        count = 1

        while stack:

            curr = stack.pop()

            for neigh, id in self.vertices[curr]:
                if not visited[neigh] and id not in banned_vertices:
                    visited[neigh] = True
                    count += 1
                    stack.append(neigh)

        return count == self.n


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        graph = Graph(n)

        for i in range(1, m+1):
            a, b = map(int, f.readline().split())
            graph.add_edge(a, b, i)

        k = int(f.readline().strip())

        for _ in range(k):
            c, *args = map(int, f.readline().split())

            banned = set(args)

            res = graph.is_connected(banned)

            if res:
                print('Connected')

            else:
                print('Disconnected')