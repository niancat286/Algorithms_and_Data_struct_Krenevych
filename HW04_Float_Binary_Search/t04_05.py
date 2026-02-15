import math

eps = 1e-11


def argument(f, m, l, r, eps, c):
    return r - l > eps


def neighbours(f, m, l, r, eps, c):
    return m != l and m != r


condition = argument


def solve(f, a, b, c):
    global eps

    left = a
    right = b

    m = (left + right) / 2.0

    while condition(f, m, left, right, eps, c):
        if f(m) < c:
            left = m
        else:
            right = m

        m = (left + right) / 2.0

    return m


f = lambda x: x*x*x + 4 * x*x + x - 6


if __name__ == "__main__":
    a = 0
    b = 2
    c = 0
    print(f"{solve(f, a, b, c):.11f}")


# x = 1.00000000000