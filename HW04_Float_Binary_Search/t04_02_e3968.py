import math


eps = 0.000001


def argument(f, m, l, r, eps, c):
    return r - l > eps


condition = argument


def solve(f, c):
    global eps

    left = 0
    right = c+eps

    m = (left + right) / 2.0

    while condition(f, m, left, right, eps, c):
        if f(m) < c:
            left = m
        else:
            right = m

        m = (left + right) / 2.0

    return m


f = lambda x: x*x + math.sqrt(x)


if __name__ == "__main__":
    c = float(input())
    print(f"{solve(f, c):.6f}")

