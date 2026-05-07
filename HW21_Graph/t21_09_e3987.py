if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        neighbors = [set() for _ in range(n + 1)]

        for _ in range(m):
            u, v = map(int, f.readline().split())

            if u != v:
                neighbors[u].add(v)
                neighbors[v].add(u)

        flag = True

        for i in range(1, n+1):
            if len(neighbors[i]) != n-1:
                flag = False
                break

        if flag:
           print("YES")
        else:
           print("NO")