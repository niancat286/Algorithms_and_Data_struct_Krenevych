import sys

input = sys.stdin.readline()


def condition(dist, n, k, coordinate):

    count = 1
    last_pos = coordinate[0]

    for i in range(1, n):
        if (coordinate[i] - last_pos) >= dist:
            count += 1
            last_pos = coordinate[i]

        if count == k:
            return True

    return False



def solve(n, k, coordinate):
    low = 0
    high = coordinate[-1] - coordinate[0]
    ans = 0

    dist = low + (high - low) // 2

    while low <= high:
        if condition(dist, n, k, coordinate):
            ans = dist
            low = dist + 1

        else:
            high = dist - 1

    return ans


if __name__ == "__main__":
    n, k = list(map(int, input.split()))
    coordinate = list(map(int, input.split()))

    print(solve(n, k, coordinate))