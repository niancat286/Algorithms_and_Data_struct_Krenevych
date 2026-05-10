from collections import deque


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix

    def min_dist(self, start, finish):
        n = len(self.matrix)
        distances = [-1 for i in range(n)]

        queue = deque()
        distances[start] = 0
        queue.append(start)

        while queue:

            curr = queue.popleft()
            if  curr == finish:
                return distances[curr]

            for j in range(n):
                if self.matrix[curr][j] == 1 and distances[j] == -1:
                    distances[j] = distances[curr] + 1
                    queue.append(j)


        return -1

    def get_all_distances(self, start):
        n = len(self.matrix)
        distances = [-1 for _ in range(n)]

        queue = deque()
        distances[start] = 0
        queue.append(start)

        while queue:
            curr = queue.popleft()

            for j in range(n):
                if self.matrix[curr][j] == 1 and distances[j] == -1:
                    distances[j] = distances[curr] + 1
                    queue.append(j)

        return distances



if __name__ == "__main__":
    with open("input.txt") as f:
        n, start = map(int, f.readline().split())

        matrix = []
        for _ in range(n):
            matrix.append(
                list(map(int, f.readline().split()))
            )

        graph = Graph(matrix)

        distances = graph.get_all_distances(start - 1)
        print(*distances)