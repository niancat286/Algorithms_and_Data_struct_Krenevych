import math

eps = 1e-11


def argument(f, m, l, r, eps, c):
    return r - l > eps


def neighbours(f, m, l, r, eps, c):
    return m != l and m != r


condition = neighbours


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


f = lambda x: x/3 - math.sin(x)


if __name__ == "__main__":
    a = 1.6
    b = 3
    c = 0
    print(f"{solve(f, a, b, c):.11f}")


# x = 2.27886266008