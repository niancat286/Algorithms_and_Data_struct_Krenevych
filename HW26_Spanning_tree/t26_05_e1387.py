import sys
import math

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()

    idx = 0
    while idx < len(input_data):
        n = int(input_data[idx])
        idx += 1

        if n == 0:
            break

        coords = []
        for _ in range(n):
            coords.append((int(input_data[idx]), int(input_data[idx + 1])))
            idx += 2

        # для алгоритму прима
        visited = [False] * n
        min_dist_sq = [float('inf')] * n
        min_dist_sq[0] = 0.0

        total_weight = 0.0

        for _ in range(n):
            u = -1
            best_dist_sq = float('inf')

            for i in range(n):
                if not visited[i] and min_dist_sq[i] < best_dist_sq:
                    best_dist_sq = min_dist_sq[i]
                    u = i

            visited[u] = True
            total_weight += math.sqrt(best_dist_sq)

            x1, y1 = coords[u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = coords[v]
                    dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2

                    if dist_sq < min_dist_sq[v]:
                        min_dist_sq[v] = dist_sq

        print(f"{total_weight:.2f}")