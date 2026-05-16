

class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)

    def num_of_comps(self):

        count = 0

        remaining = list(range(self.n))
        while remaining:
            count += 1
            start = remaining.pop()

            stack = [start]

            while stack:

                curr = stack.pop()

                for j in range(self.n):
                    if self.matrix[curr][j] == 1 and j in remaining:
                        stack.append(j)
                        remaining.remove(j)

        return count


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int, f.readline().split())) for _ in range(n)
        ]
        graph = Graph(matrix)

        print(graph.num_of_comps())