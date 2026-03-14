import math
import re
import sys


EMPTY = "EMPTY"

def is_prime(n):

    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0:
            return False

    return True


class Set:

    M = 31

    def __init__(self,size: int = 11):
        self.size = size
        self.count = 0
        self.words: list[EMPTY | str] = [EMPTY for _ in range(size)]


    def hash(self,key):

        h = 0
        for s in key:
            h = (h * self.M + ord(s)) % self.size

        return h


    def rehash(self):
        self.size = self.size * 2 + 1
        while not is_prime(self.size):
            self.size += 2

        words = self.words

        self.__init__(self.size)

        for i in range(len(words)):
            if words[i] is not EMPTY:
                self.add(words[i])

    def add(self, word):

        if self.count > self.size * 0.7:
            self.rehash()

        h = self.hash(word)
        while self.words[h] is not EMPTY:

            if self.words[h] == word:
                return

            h = (h + 1) % self.size

        self.words[h] = word
        self.count += 1

    def get(self, word):

        h = self.hash(word)

        while self.words[h] is not EMPTY:
            if self.words[h] == word:
                return self.words[h]

            h = (h + 1) % self.size


    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return False if self.get(key) is None else True

    def __iter__(self):
        res = []
        for i in range(self.size):
            if self.words[i] is not EMPTY:
                res.append(self.words[i])

        return iter(res)


if __name__ == "__main__":

    dct = Set()

    for line in sys.stdin:
        # print("--->")
        words = re.findall(r'[a-zA-Z]+',line)
        # print(words)
        for word in words:
            word = word.lower()
            if word not in dct:
                dct.add(word)

    print(*sorted(dct),sep="\n")

    # words = set()
    # f = open("input1.txt")
    #
    #
    # for line in f:
    # # while True:
    # #     try:
    # #         line = input()
    # #     except EOFError:
    # #         break
    #
    #     word = ""
    #     for s in line:
    #         if s.isalpha():
    #             word += s.lower()
    #         elif word:
    #             words.add(word)
    #             word = ""
    #
    #     # if word:
    #     #     words.add(word)
    #
    # print(*sorted(words),sep="\n")
    # # print(*words,sep="\n")
    #
    # f.close()


