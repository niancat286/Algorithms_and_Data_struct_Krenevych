import math
import sys

EMPTY = None


class Set:
    def __init__(self,size: int = 300007):
        self.size = size
        self.count = 0
        self.numbers = [EMPTY] * size

    def hash(self, key):
        return key % self.size

    def add(self, num):
        h = self.hash(num)
        while self.numbers[h] is not EMPTY:

            if self.numbers[h] == num:
                return

            h = (h + 1) % self.size

        self.numbers[h] = num
        self.count += 1


def solution():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    dct = Set()
    for i in range(1, len(input_data)):
        num = int(input_data[i])
        dct.add(num)

    print(dct.count)


if __name__ == "__main__":
    solution()