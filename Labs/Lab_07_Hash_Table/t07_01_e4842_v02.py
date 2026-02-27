import math

EMPTY = "EMPTY"

class Dict:

    M = 31
    def __init__(self, size: int = 11):
        self.size = size
        self._keys: [EMPTY | str] = [EMPTY for _ in range(self.size)]
        self._values: [EMPTY | list(str)] = [EMPTY for _ in range(self.size)]
        self.count = 0

    def is_prime(self, n: int):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def rehash(self):
        self.size = self.size * 2 +1
        while not self.is_prime(self.size):
            self.size += 2

        _keys = self._keys
        _values = self._values

        self.__init__(self.size)

        for i in range(len(_keys)):
            if _keys[i] is not EMPTY:
                self.set(_keys[i], _values[i])

    def hash(self, key: str):
        h = 0
        for i in range(len(key)):
            h = (h * self.M + ord(key[i])) % self.size

        return h

    def set(self, key, value):
        if self.size * 0.7 < self.count:
            self.rehash()


        i = self.hash(key)

        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                self._values[i] = value

            i = (i + 1) % self.size

        self._keys[i] = key
        self._values[i] = value
        self.count += 1

    def get(self, key):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return self._values[i]

            i = (i + 1) % self.size

    def keys(self):
        key_list = []
        for i in range(self.size):
            if self._keys[i] is not EMPTY:
                key_list.append(self._keys[i])

        return key_list


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
        print(*dct[latin], sep=", ")