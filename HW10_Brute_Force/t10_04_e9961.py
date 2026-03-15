

def solve(n, k, current):
    if len(current) == k:
        print(*current)
        return

    for i in range(1, n+1):
        if i not in current:
            current.append(i)
            solve(n, k, current)
            current.pop()


if __name__ == "__main__":
    n, k = map(int, input().split())
    solve(n, k, [])
