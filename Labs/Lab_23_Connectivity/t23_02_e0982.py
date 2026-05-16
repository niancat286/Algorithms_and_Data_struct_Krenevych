

class Graph:

    def __init__(self, n):
        self.vertices = { i : set() for i in range(1, n+1)}

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def is_connected(self):

        remaining = set(self.vertices)

        stack = [remaining.pop()]

        while stack:

            curr = stack.pop()

            for neigh in self.vertices[curr]:
                if neigh in remaining:
                    stack.append(neigh)
                    remaining.remove(neigh)

        return len(remaining) == 0

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        graph = Graph(n)

        for _ in range(m):
            a, b = map(int, f.readline().split())
            graph.add_edge(a, b)


        res = graph.is_connected()
        #print()

        if res:
            print('YES')

        else:
            print('NO')