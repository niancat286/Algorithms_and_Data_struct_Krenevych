
# postfix
# 3 + 2 * 3     == 3 2 3 + *
# (3 + 2) * 3   == 3 2 + 3 *

#prefix
# 3 + 2 * 3     == + 3 * 2 3
# (3 + 2) * 3   == * + 3 2 3



OPERATORS = "+-*/"


def evaluate(expr: str) -> str:
    stack = []

    for token in reversed(expr):
        if token in OPERATORS:
            a, a_power = stack.pop()
            b, b_power = stack.pop()

            if token in "+-":
                power = 1
            else:
                power = 2

            if a_power < power:
                a = f"({a})"

            if b_power < power or (b_power == power and token in "-/"):
                b = f"({b})"

            tmp = f"{a}{token}{b}"


            stack.append((tmp, power))

        else:
            stack.append((token, 3))

    return stack.pop()[0]


if __name__ == "__main__":
    expr = input()
    print(evaluate(expr))