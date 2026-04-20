

class EmployeeTree:
    def __init__(self, fee: int):
        self.fee = fee
        self.children: list['EmployeeTree'] = []

    def add_child(self, item: 'EmployeeTree'):
        self.children.append(item)

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def DFS_min_cost(self) -> int:
        """ Обхід дерева в глибину"""

        if self.is_leaf():
            return self.fee

        min_child_cost = min(child.DFS_min_cost() for child in self.children)

        return self.fee + min_child_cost


def solve():
    nodes = []
    links = {}
    n = 0
    line_num = 0

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line_num == 0:
                n = int(line)
                nodes = [None] * (n + 1)

            else:
                i = line_num

                fee, k, *children_ids = map(int, line.split())

                nodes[i] = EmployeeTree(fee)
                links[i] = children_ids

            line_num += 1

            if line_num > n:
                break

    for i in range(1, n + 1):
        if nodes[i] is not None:
            for child_id in links[i]:
                nodes[i].add_child(nodes[child_id])

    if n >= 1 and nodes[1] is not None:
        print(nodes[1].DFS_min_cost())


if __name__ == "__main__":
    solve()