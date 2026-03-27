BRACKETS = {"(" : ")", "[" : "]"}



def check(seq: str) -> bool:
    stack = []

    for bracket in seq:
        if bracket not in BRACKETS:
            if len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
                return False
        else:
            stack.append(bracket)

    return len(stack) == 0


if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline())

        for _ in range(n):
            seq = f.readline().strip()
            if check(seq):
                print('Yes')
            else:
                print('No')
