import sys

EMPTY = None
M = 31


class Set:

    def __init__(self,size: int = 300007):
        self.size = size
        self.count = 0
        self.words = [EMPTY] * size

    def hash(self, key):
        global M
        h = 0
        for i in range(len(key)):
            h = (h * M + ord(key[i])) % self.size

        return h

    def add(self, word):
        h = self.hash(word)
        while self.words[h] is not EMPTY:

            if self.words[h] == word:
                return

            h = (h + 1) % self.size

        self.words[h] = word
        self.count += 1

    def contains(self, word: str) -> bool:
        h = self.hash(word)
        while self.words[h] is not EMPTY:
            if self.words[h] == word:
                return True
            h = (h + 1) % self.size
        return False


def solution():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    line1 = input_data[0].split()
    n = int(line1[0])
    m = int(line1[1])

    dct = Set()
    for i in range(1, n+1):
        dct.add(input_data[i].strip().lower())

    text = " ".join(input_data[n + 1: n + 1 + m]).lower()

    punctuation = {'.', ',', ':', ';', '-', "'", '"', '!', '?'}
    used = Set()
    curr = []

    def check_word(chars):
        word = "".join(chars)
        if not dct.contains(word):
            return False
        used.add(word)
        return True

    for char in text:
        if char in punctuation or char.isspace():
            if curr:
                if not check_word(curr):
                    print("Some words from the text are unknown.")
                    return
                curr = []
        else:
            curr.append(char)

    if curr:
        if not check_word(curr):
            print("Some words from the text are unknown.")
            return

    if used.count < dct.count:
        print("The usage of the vocabulary is not perfect.")
    else:
        print("Everything is going to be OK.")


if __name__ == "__main__":
    solution()
