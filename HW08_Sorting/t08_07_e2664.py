def sort_insertion(array):
    n = len(array)

    is_sorted = True
    for k in range(n - 1):
        if array[k] > array[k + 1]:
            is_sorted = False
            break

    if is_sorted:
        return

    for i in range(1, n):
        pos = i
        x = array[pos]

        changed = False

        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
                changed = True
            else:
                break
            pos -= 1

        array[pos] = x

        if changed:
            print(*array)


if __name__ == "__main__":

    n = int(input())
    array = list(map(int, input().split()))
    #array = [9, 1, -1, 20, 19, 10, -5, 13, 7]

    sort_insertion(array)