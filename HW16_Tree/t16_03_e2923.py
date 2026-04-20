import sys
sys.setrecursionlimit(2000000)



class Tree:
    def __init__(self, id:int, color:int):
        self.id = id
        self.color = color

        self.children: list["Tree"] = []
        self.count = 0

    def add_child(self, child: "Tree"):
        self.children.append(child)

    def calc_colors(self) -> set[int]:
        my_colors = {self.color}

        for ch in self.children:
            child_colors = ch.calc_colors()

            if len(child_colors) > len(my_colors):
                my_colors, child_colors = child_colors, my_colors

            my_colors.update(child_colors)

        self.count = len(my_colors)
        return my_colors


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])

    nodes = [None] * (n + 1)
    parents = [0] * (n + 1)

    idx = 1
    for i in range(1, n + 1):
        p_i = int(input_data[idx])
        c_i = int(input_data[idx + 1])
        idx += 2

        nodes[i] = Tree(i, c_i)
        parents[i] = p_i

    root = None
    for i in range(1, n + 1):
        p_i = parents[i]
        if p_i == 0:
            root = nodes[i]
        else:
            nodes[p_i].add_child(nodes[i])

    if root:
        root.calc_colors()

    for i in range(1, n + 1):
        print(nodes[i].count, end=" ")
    print()


if __name__ == "__main__":
    solve()

