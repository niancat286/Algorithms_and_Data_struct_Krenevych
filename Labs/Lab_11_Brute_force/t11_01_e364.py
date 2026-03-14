

alphabet: list[str]
k: int
count: int = 0
n: int


def solve(word: str) -> str:
    global count



    if len(word) == n:
        count += 1
        #print(count, word)
        return word


    for letter in alphabet:
        if letter not in word:
            res = solve(word + letter)
            if count == k:
                return res



if __name__ == "__main__":
    n, k = map(int, input().split())

    alphabet = [chr(ord("a") + i) for i in range(n)]

    #print(alphabet)

    print(solve(""))