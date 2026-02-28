def sort(array):
    count = 0
    n = len(array)
    for j in range(n, 0, -1):
        for i in range(1, j):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    res = sort(array)
    print(res)
