if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split())

        seen_edges = set()
        flag = False

        for _ in range(m):
            u, v = map(int, f.readline().split())

            if (u, v) in seen_edges:
                flag = True
                break

            seen_edges.add((u, v))

        if flag:
           print("YES")
        else:
           print("NO")