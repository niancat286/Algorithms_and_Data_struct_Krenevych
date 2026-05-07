

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        degree = [0] * (n+1)

        for _ in range(m):
            u, v = map(int, f.readline().split())

            degree[u] += 1
            degree[v] += 1

        for i in range(1, n+1):
            print(f"{degree[i]}")