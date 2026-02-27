import math

EMPTY = "EMPTY"

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class Dict:

    M = 31

    def __init__(self,size: int = 1000003):
        self.size = size
        self._slots: [None | Node] = [None for _ in range(self.size)]


    # C0*M^n+ C1*M^{n-1} + C2*M^{n-2} + C3*M^{n-3} + .... +Cn-2*M +Cn-1

    def hash(self,key: str):
        h = 0
        for i in range(len(key)):
            h = (h * self.M + ord(key[i])) % self.size

        return h

    def set(self,key,value):


        i = self.hash(key)
        node = self._slots[i]
        while node is not None:
            if node.key == key:
                node.value = value
                return
            node = node.next

        node = Node(key, value)
        node.next = self._slots[i]
        self._slots[i] = node

    def get(self, key):

        i = self.hash(key)
        node = self._slots[i]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next


    def keys(self):
        keys_list = []
        for i in range(self.size):
            node  = self._slots[i]
            while node is not None:
                keys_list.append(node.key)
                node = node.next


        return keys_list

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True

if __name__ == "__main__":

    f = open("input.txt")
    dct = Dict()
    for line in f:
        eng, latin = line.strip().split(" - ")
        latins = latin.split(", ")
        for latin in latins:
            if latin in dct:
                dct[latin].append(eng)
            else:
                dct[latin] = [eng]

    latins_sorted = sorted(dct.keys())
    print(len(latins_sorted))

    for latin in latins_sorted:
        print(latin, end= " - ")
        print(*dct[latin], sep= ", ")

