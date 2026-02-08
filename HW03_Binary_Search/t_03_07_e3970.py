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

    index = left - 1

    if index >= 0 and index < len(arr) and arr[index] == x:
        return index
    else:
        return -1


def binary_search_left(arr, x):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        #print(f"left: {left}, right: {right}, mid: {mid}")

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left


def solve():
    n = int(input())
    array_full = list(map(int, input().split()))

    m = int(input())
    array_find = list(map(int, input().split()))

    for x in array_find:
        res_r = binary_search_right(array_full, x)
        res_l = binary_search_left(array_full, x)

        res = res_r - res_l + 1
        if res < 0:
            print(0)
        else:
            print(res)



if __name__ == '__main__':
    solve()