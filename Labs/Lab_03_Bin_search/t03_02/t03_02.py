
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        print(f"left: {left}, right: {right}, mid: {mid}")

        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid

    return left



if __name__ == "__main__":
    array = [1,2,3,4,4,5,6,6,7,7,8]

    x = 4
    print(binary_search(array, x))