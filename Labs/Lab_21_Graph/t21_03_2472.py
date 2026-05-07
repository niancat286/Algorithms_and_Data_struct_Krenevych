if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())
        k = int(f.readline().strip())

        adjList = {v : [] for v in range(1,n + 1)}
        for _ in range(k):
            cmd_id, *args = list(map(int,f.readline().split()))

            if cmd_id == 1:
                adjList[args[0]].append(args[1])
                adjList[args[1]].append(args[0])
            elif cmd_id == 2:
                print(*adjList[args[0]])