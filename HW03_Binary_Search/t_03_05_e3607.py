import sys


def count_num(n, arr, a, b):
    counter = 0
    for i in range(n):      #просто лінійний пошук
        if (arr[i] >= a) and (arr[i] <= b):
            counter += 1

    return counter


def solve():
    while True:
        line = sys.stdin.readline()

        if not line:
            break

        n = int(line)

        arr_line = sys.stdin.readline().split()
        arr = [int(x) for x in arr_line]

        bounds_line = sys.stdin.readline().split()
        a = int(bounds_line[0])
        b = int(bounds_line[1])

        print(count_num(n, arr, a, b))


if __name__ == '__main__':
    solve()
