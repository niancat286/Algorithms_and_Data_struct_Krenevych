def sort_insertion(array):

    n = len(array)

    for i in range(1, n):
        pos = i
        x = array[pos]
        while pos > 0:
            if array[pos - 1] > x:
                array[pos] = array[pos - 1]
            else:
                break
            pos -= 1
        array[pos] = x


if __name__ == "__main__":
    n = int(input())
    times = []
    for _ in range(n):
        time_moment = list(map(int, input().split()))
        times.append(time_moment)

    sort_insertion(times)

    for time_moment in times:
        print(*time_moment)