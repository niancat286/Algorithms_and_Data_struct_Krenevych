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


def solve():
    n = int(input())
    array_full = list(map(int, input().split()))

    m = int(input())
    array_find = list(map(int, input().split()))

    for x in array_find:
        res = binary_search_right(array_full, x)
        if array_full[res] == x:
            print('YES')
        else:
            print("NO")



if __name__ == '__main__':
    solve()