import sys
from math import log2, ceil, gcd


class Segment_Tree:
    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k)) if k > 0 else 1

        self.items = [0] * n + array + [0] * (n - k)
        #print(self.items)

        for i in range(n - 1, 0, -1):
            self.items[i] = gcd(self.items[2 * i], self.items[2 * i + 1])

        #print(self.items)

        self.size = n

    def update(self, pos, new_value):

        pos += self.size

        self.items[pos] = new_value
        while pos > 1:
            pos //= 2
            self.items[pos] = gcd(self.items[2 * pos], self.items[2 * pos + 1])

        #print(self.items)

    def get_gcd(self, from_idx, to_idx):
        left = from_idx + self.size
        right = to_idx + self.size

        result = 0

        while left <= right:

            if left % 2 == 1:
                result = gcd(result, self.items[left])
                left += 1

            if right % 2 == 0:
                result = gcd(result, self.items[right])
                right -= 1

            left //= 2
            right //= 2

        return result



if __name__ == "__main__":
    data = sys.stdin.read().split()

    if data:
        n = int(data[0])
        array = [int(x) for x in data[1:n + 1]]
        tree = Segment_Tree(array)
        m = int(data[n + 1])
        idx = n + 2
        out = []
        for _ in range(m):
            q = int(data[idx])
            l = int(data[idx + 1])
            r = int(data[idx + 2])
            idx += 3

            if q == 1:
                result = tree.get_gcd(l - 1, r - 1)
                out.append(str(result))
            elif q == 2:
                tree.update(l - 1, r)
        sys.stdout.write('\n'.join(out) + '\n')
