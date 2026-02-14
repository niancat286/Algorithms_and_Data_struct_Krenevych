def solve(n, w, h):

    low = 1
    high = n * max(w, h)

    while low < high:
        a = low + (high - low) // 2
        count = (a // h) * (a // w)     #f(x)

        if count < n:
            low = a + 1
        else:
            high = a


    return low


if __name__ == "__main__":
    w, h, n = list(map(int, input().split()))
    print(solve(n, w, h))