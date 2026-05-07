class Graph:
    def __init__(self, matrix):
        self.adjency = matrix

    def edges(self):
        res = []
        for i in range(len(self.adjency)):
            for j in range(i, len(self.adjency)):
                if self.adjency[i][j] == 1:
                    res.append((i+1, j +1))

        return res


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = []
        for i in range(n):
            row = list(map(int, f.readline().split()))
            matrix.append(row)

        graph = Graph(matrix)

        edges = graph.edges()

        for edge in edges:
            print(*edge)
