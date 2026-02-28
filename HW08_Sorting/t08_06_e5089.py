def sort_buble(array):
    n = len(array)
    for j in range(n, 0, -1):
        for i in range(1, j):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]


def sort_selection(array):
    n = len(array)
    for j in range(n - 1, 0, -1):
        pos = 0
        for i in range(1, j + 1):
            if array[i] > array[pos]:
                pos = i
        array[pos], array[j] = array[j], array[pos]
        #print(array)


if __name__ == "__main__":
    n = int(input())
    array = []
    for i in range(n):
        array.append(input())

    sort_selection(array)
    for j in range(n):
        print(array[j])