import sys

sys.set_int_max_str_digits(400000)


def multipl(A, B):
    result = 0
    for _ in range(B):
        result += A
    return result


def karatsuba(x, y):

    if x < 16 or y < 16:
        return multipl(x, y)

    m = max(x.bit_length(), y.bit_length()) // 2

    mask = (1 << m) - 1

    x0 = x & mask
    x1 = x >> m
    y0 = y & mask
    y1 = y >> m

    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1 + x0, y1 + y0)

    return (z2 << (2 * m)) + ((z1 - z2 - z0) << m) + z0


def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return

    a = int(input_data[0])
    b = int(input_data[1])

    result = karatsuba(a, b)

    print(result)


if __name__ == '__main__':
    solve()