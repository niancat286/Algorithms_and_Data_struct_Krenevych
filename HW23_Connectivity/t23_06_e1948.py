import sys

sys.setrecursionlimit(20000)


WHITE = 0
BLACK = 1
GRAY = 2

class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = [[] for _ in range(n+1)]

    def add_edge(self, v1, v2):
        self.vertices[v1].append(v2)

    def dfs(self):
        colors = [WHITE] * (self.n + 1)
        visited = []

        for i in range(1, self.n + 1):
            if colors[i] == WHITE:
                if self.dfs_helper(i, visited, colors):
                    print('-1')
                    return True

        print(*visited[::-1])
        return False

    def dfs_helper(self, vertex, visited, colors):

        colors[vertex] = GRAY

        #print(f"--> {vertex}")

        for neigh in self.vertices[vertex]:
            if colors[neigh] == WHITE:
                if self.dfs_helper(neigh, visited, colors):
                    return True
            elif colors[neigh] == GRAY:
                return True


        #print(f"<-- {vertex} (exit)")
        visited.append(vertex)
        colors[vertex] = BLACK
        return False


if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        graph = Graph(n)

        for _ in range(m):
            v1, v2 = map(int, f.readline().split())
            graph.add_edge(v1, v2)



        graph.dfs()