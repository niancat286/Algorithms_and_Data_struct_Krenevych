def solve(nums: list[int]):
    for i in range(len(nums)):
        el = nums[i]
        sub_nums = nums[: i] + nums[i+1 :]
        if _solve(sub_nums, el):
            return True
    return False


def _solve(nums: list[int], value: int):
    #print(nums, value)

    if len(nums) == 0:
        return value == 23

    for i in range(len(nums)):
        el = nums[i]
        sub_nums = nums[: i] + nums[i+1 :]

        if _solve(sub_nums, value + el):
            return True
        if _solve(sub_nums, value - el):
            return True
        if _solve(sub_nums, value * el):
            return True

    return False


if __name__ == "__main__":

    f = open("input.txt")
    for line in f:
        nums = [int(x) for x in line.split()]

        if nums == [0] * 5:
            break

        #print(*nums)
        if solve(nums):
            print('Possible')
        else:
            print('Impossible')

    f.close()