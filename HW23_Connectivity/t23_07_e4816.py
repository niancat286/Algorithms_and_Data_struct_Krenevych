

class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = [[] for _ in range(n+1)]

    def add_edge(self, v1, v2):
        self.vertices[v1].append(v2)
        self.vertices[v2].append(v1)

    def num_of_comps(self):

        compon = []

        visited = [False] * (self.n + 1)
        for i in range(1, self.n + 1):
            if not visited[i]:
                curr_comp = []

                stack = [i]
                visited[i] = True

                while stack:

                    curr = stack.pop()
                    curr_comp.append(curr)

                    for neigh in self.vertices[curr]:
                        if not visited[neigh]:
                            visited[neigh] = True
                            stack.append(neigh)

                compon.append(curr_comp)


        return compon


if __name__ == "__main__":
    res = []
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        graph = Graph(n)

        for _ in range(m):
            v1, v2 = map(int, f.readline().split())
            graph.add_edge(v1, v2)

        comps = graph.num_of_comps()

        res.append(str(len(comps)))

        for el in comps:
            res.append(str(len(el)))
            res.append(" ".join(map(str, el)))
        print("\n".join(res))



