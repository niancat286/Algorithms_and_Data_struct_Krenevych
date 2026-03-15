import sys


best_sum = 0
best_path = []
N = 0
tracks = []
visited = set()


def solve(index, cur_sum, cur_path):
    global best_sum, best_path, N, tracks

    if cur_sum == N:
        best_sum = cur_sum
        best_path = cur_path.copy()
        return

    if index == len(tracks):
        if cur_sum > best_sum:
            best_sum = cur_sum
            best_path = cur_path.copy()
        return

    state = (index, cur_sum)
    if state in visited:
        return
    visited.add(state)

    if cur_sum + tracks[index] <= N:
        cur_path.append(tracks[index])
        solve(index + 1, cur_sum + tracks[index], cur_path)
        cur_path.pop()

    solve(index + 1, cur_sum, cur_path)


def _solve():
    global best_sum, best_path, N, tracks, visited

    for line in sys.stdin:
        nums = list(map(int, line.split()))
        if not nums:
            continue

        N = nums[0]
        tracks = nums[2:]

        best_sum = 0
        best_path = []
        visited.clear()

        solve(0, 0, [])

        #for track in best_path:
            #print(track, end=" ")
        #print()
        print(f"sum:{best_sum}")


if __name__ == "__main__":
    _solve()