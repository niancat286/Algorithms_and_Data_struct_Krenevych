WHITE = 0
BLACK = 1
GRAY = 2

class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def dfs(self):
        colors = [WHITE] * self.n
        visited = []

        for i in range(self.n):
            if colors[i] == WHITE:
                if self.dfs_helper(i, visited, colors):
                    return True

        print(visited[::-1])
        return False

    def dfs_helper(self, vertex, visited, colors):

        colors[vertex] = GRAY

        print(f"--> {vertex + 1}")

        for j in range(self.n):
            if self.matrix[vertex][j] == 1:
                if colors[j] == WHITE:
                    if self.dfs_helper(j, visited, colors):
                        return True
                elif colors[j] == GRAY:
                    return True


        print(f"<-- {vertex + 1} (exit)")
        visited.append(vertex + 1)
        colors[vertex] = BLACK
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int, f.readline().split())) for _ in range(n)
        ]

        graph = Graph(matrix)
        print(graph.dfs())