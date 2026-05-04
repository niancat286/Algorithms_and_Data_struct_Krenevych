import sys
from math import log2, ceil, gcd


class Segment_Tree:
    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k)) if k > 0 else 1

        INF = float("inf")

        self.tree_min = [INF] * n + array + [INF] * (n - k)
        self.tree_max = [0] * n + array + [0] * (n - k)


        for i in range(n - 1, 0, -1):
            self.tree_min[i] = min(self.tree_min[2 * i], self.tree_min[2 * i + 1])
            self.tree_max[i] = max(self.tree_max[2 * i], self.tree_max[2 * i + 1])
        #print(self.items)

        self.size = n

    def update(self, pos, new_value):

        pos += self.size

        self.tree_min[pos] = new_value
        self.tree_max[pos] = new_value

        while pos > 1:
            pos //= 2
            self.tree_min[pos] = min(self.tree_min[2 * pos], self.tree_min[2 * pos + 1])
            self.tree_max[pos] = max(self.tree_max[2 * pos], self.tree_max[2 * pos + 1])
        #print(self.items)

    def check_eq(self, from_idx, to_idx):
        left = from_idx + self.size
        right = to_idx + self.size

        res_min = float('inf')
        res_max = 0

        while left <= right:

            if left % 2 == 1:
                if self.tree_min[left] < res_min: res_min = self.tree_min[left]
                if self.tree_max[left] > res_max: res_max = self.tree_max[left]
                left += 1

            if right % 2 == 0:
                if self.tree_min[right] < res_min: res_min = self.tree_min[right]
                if self.tree_max[right] > res_max: res_max = self.tree_max[right]
                right -= 1

            left //= 2
            right //= 2

        return res_min == res_max



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
                real_l, real_r = min(l, r), max(l, r)

                if tree.check_eq(real_l - 1, real_r - 1):
                    out.append("draw")
                else:
                    out.append("wins")
            elif q == 2:
                tree.update(l - 1, r)
        sys.stdout.write('\n'.join(out) + '\n')
