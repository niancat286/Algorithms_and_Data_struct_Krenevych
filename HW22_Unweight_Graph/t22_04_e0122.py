import sys

sys.setrecursionlimit(200000)


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    k = int(input_data[1])
    start_node = int(input_data[2])
    target_node = int(input_data[3])
    max_days = int(input_data[4])

    graph = {i: [] for i in range(1, n + 1)}

    idx = 5
    for _ in range(k):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        if u in graph:
            graph[u].append(v)
        idx += 2

    visited = [False] * (n + 1)

    def dfs(curr, days_spent):
        if days_spent > max_days:
            return 0

        if curr == target_node:
            return 1

        paths_count = 0
        visited[curr] = True

        for neighbor in graph[curr]:
            if not visited[neighbor]:
                paths_count += dfs(neighbor, days_spent + 1)

        visited[curr] = False

        return paths_count

    total_routes = dfs(start_node, 0)
    print(total_routes)


if __name__ == "__main__":
    solve()