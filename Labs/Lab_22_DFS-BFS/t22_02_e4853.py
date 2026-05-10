from collections import deque


class Graph:
    def __init__(self, n):
        self.vertices = {i: set() for i in range(1, n+1)}

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def shortest_path(self, start, finish):
        source = {start: None}
        queue = deque()
        queue.append(start)

        while queue:
            curr = queue.popleft()

            if curr == finish:
                break

            for neigh in self.vertices[curr]:
                if neigh not in source:
                    source[neigh] = curr
                    queue.append(neigh)

        else:
            return []

        path = [finish]

        curr = finish

        while source[curr] is not None:
            curr = source[curr]
            path.append(curr)

        return path[::-1]


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())
        start, finish = map(int, f.readline().split())

        graph = Graph(n)

        for _ in range(m):
            a, b = map(int, f.readline().split())

            graph.add_edge(a, b)

        path = graph.shortest_path(start, finish)
        print(len(path) - 1)
        print(*path)