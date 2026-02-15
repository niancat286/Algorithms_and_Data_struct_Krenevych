eps = 0.000001


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


f = lambda x: x*x*x + x + 1

if __name__ == "__main__":
    a = 0
    b = 10
    c = 5
    print(f"{solve(f, a, b, c):.6f}")


# if condition == argument  --> x = 1.378797
# if condition == neighbore --> x = 1.378797