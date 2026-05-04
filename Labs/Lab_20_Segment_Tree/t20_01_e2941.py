from math import log2, ceil


class Segment_Tree:
    def __init__(self, array):

        k = len(array)
        n = 1 << ceil(log2(k))

        self.items = [0] * n + array + [0] * (n - k)
        #print(self.items)

        for i in range(n - 1, 0, -1):
            self.items[i] = self.items[2 * i] + self.items[2 * i + 1]

        #print(self.items)

        self.size = n

    def update(self, pos, new_value):

        pos += self.size

        self.items[pos] = new_value
        while pos > 1:
            pos //= 2
            self.items[pos] = self.items[2 * pos] + self.items[2 * pos + 1]

        #print(self.items)

    def sum(self, from_idx, to_idx):
        left = from_idx + self.size
        right = to_idx + self.size

        result = 0

        while left <= right:

            if left % 2 == 1:
                result += self.items[left]
                left += 1

            if right % 2 == 0:
                result += self.items[right]
                right -= 1

            left //= 2
            right //= 2

            #if left == right:
            #    result = self.items[left]
            #    break
        return result



if __name__ == "__main__":
    #array = [2, 3, 8, 5, 9, 1]
    #кількість елементів не степінь двійки, тому доповнимо нейтральними елементами
    #array = [2, 3, 8, 5, 9, 1, 0, 0]
    #array = [0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 8, 5, 9, 1, 0, 0]
    #array = [0, 28, 18, 10, 5, 13, 10, 0, 2, 3, 8, 5, 9, 1, 0, 0]

    #tree = Segment_Tree(array)
    #tree.update(0, 4)
    #print(tree.sum(0, 7))


    with open("input.txt") as f:
        n,q = map(int, f.readline().split())
        array = list(map(int, f.readline().split()))
        tree = Segment_Tree(array)
        for _ in range(q):
            cmd, x, y = f.readline().split()

            x = int(x)
            y = int(y)

            if cmd == "=":
                tree.update(x - 1, y)
            elif cmd == "?":
                print(tree.sum(x-1, y-1))