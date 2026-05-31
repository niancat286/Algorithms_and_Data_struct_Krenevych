
def floyd(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        matrix = [
            list(map(int,f.readline().split()))
            for _ in range(n)
        ]

        floyd(matrix,n)

        for row in matrix:
            print(*row)