import math
import re
import sys


class Node:
    def __init__(self,word):
        self.word = word
        self.next = None

class Set:

    M = 31

    def __init__(self,size: int = 1000003):
        self.size = size
        self.slots: list[None | Node] = [None for _ in range(size)]


    def hash(self,key):

        h = 0
        for s in key:
            h = (h * self.M + ord(s)) % self.size

        return h

    def add(self, word):



        h = self.hash(word)
        node = self.slots[h]
        while node is not None:

            if node.word == word:
                return

            node = node.next

        node = Node(word)
        node.next = self.slots[h]
        self.slots[h] = node

    def get(self, word):

        h = self.hash(word)
        node = self.slots[h]
        while node is not None:

            if node.word == word:
                return node.word

            node = node.next




    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __iter__(self):
        words_list = []
        for i in range(self.size):
            node = self.slots[i]
            while node is not None:
                words_list.append(node.word)
                node = node.next

        return iter(words_list)


if __name__ == "__main__":

    dct = Set()

    for line in sys.stdin:
        words = re.findall(r'[a-zA-Z]+',line)
        for word in words:
            word = word.lower()
            if word not in dct:
                dct.add(word)

    print(*sorted(dct),sep="\n")

