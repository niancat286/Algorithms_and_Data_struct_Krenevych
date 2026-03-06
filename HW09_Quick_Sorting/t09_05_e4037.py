import sys


def _merge_sort(array, a, b):

    if a >= b:
        return

    m = a + (b - a) // 2



    _merge_sort(array,a,m)
    _merge_sort(array,m + 1,b)


    left = array[a: m + 1]

    i = 0
    j = m + 1
    k = a
    while i < len(left) and j <= b:
        if left[i][0] <= array[j][0]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = array[j]
            j += 1

        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    robots = []

    idx = 1
    for _ in range(n):
        main_num = int(input_data[idx])
        add_num = int(input_data[idx + 1])
        robots.append((main_num, add_num))
        idx += 2

    _merge_sort(robots, 0, n - 1)

    for robot in robots:
        print(f"{robot[0]} {robot[1]}")


if __name__ == '__main__':
    solve()