

def solve(n, x, y):

    first_copy = min(x, y)

    low = 0
    high = (n - 1) * max(x, y)

    while low < high:
        t = low + (high - low) // 2
        count = (t // x) + (t // y)

        if count < n - 1:
            low = t + 1
        else:
            high = t

    return low + first_copy


if __name__ == "__main__":
    n, x, y = list(map(int, input().split()))
    print(solve(n, x, y))