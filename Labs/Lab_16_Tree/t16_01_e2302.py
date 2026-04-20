




class PrefixTree:
    def __init__(self):
        self.children: dict[str : PrefixTree] = {}

    def add_child(self, d:str):
        self.children[d] = PrefixTree()

    def has_child(self, d: str):
        return d in self.children

    def get_child(self, d: str):
        return self.children[d]

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def add_phone(self, phone) -> bool:
        i = 0
        node = self


        while i < len(phone) and node.has_child(phone[i]):
            node = node.get_child(phone[i])
            i += 1

        if i == len(phone):
            return False

        if i > 0 and node.is_leaf():
            return False

        while i < len(phone):
            node.add_child(phone[i])

            node = node.get_child(phone[i])
            i += 1



        return True



