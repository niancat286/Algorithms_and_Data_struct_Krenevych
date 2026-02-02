import sys

input = sys.stdin.readline


def binary_search_right(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        #print(f"left: {left}, right: {right}, mid: {mid}")

        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left - 1



if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    array = list(map(int, input().split()))
    request_x = []

    for i in range(m):
        x = int(input())
        request_x.append(x)

    for x in request_x:
        res = binary_search_right(array, x)
        if array[res] == x:
            print(res + 1)
        else:
            print(0)
