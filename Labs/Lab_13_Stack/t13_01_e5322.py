
def convert(num: str, from_base: int , to_base: int) -> str:

    decimal = 0

    for d in num:
        decimal = decimal * from_base + int(d, from_base)

    #print(decimal)

    stack = []
    while decimal > 0:
        stack.append(
            decimal % to_base
        )

        decimal //= to_base

    res = ""
    while stack:
        res += get_char(stack.pop())

    print(res)
    return res



def get_char(n: int) -> str:
    if n < 10:
        return str(n)
    else:
        return chr(ord("A") + n - 10)

if __name__ == "__main__":
    n = input()

    convert(n, 2, 16)













