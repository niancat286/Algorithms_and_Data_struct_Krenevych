


class Graph:
    def __init__(self, n: int):

        self.edges = {v : [] for v in range(1, n+1)}

    def addEdges(self, from_idx, to_idx):
        self.edges[from_idx].append(to_idx)

    def agjency_matrix(self) -> list(list[int]):
        matrix = [[0 * len(self.edges)] for _ in range(len(self.edges))]

        for v in self.edges.keys():
            for neighbour in self.edges[v]:
                i = v - 1
                j = neighbour - 1
                matrix[i][j] = 1

        return matrix


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        graph = Graph(n)

        for row in range(n):
            data = list(map(int, f.readline().split()))
            if data[0] > 0:
                N = data[0]
                for i in range(1, N + 1):
                    graph.addEdges(row + 1, data[i])

        matrix = graph.agjency_matrix()




