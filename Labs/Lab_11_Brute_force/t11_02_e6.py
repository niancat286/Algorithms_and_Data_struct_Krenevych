
max_income: int = 0



def solve(vouchers: list[tuple[int]], income: int, day: int):
    global max_income

    #print(vouchers, income, day)

    if len(vouchers) == 0 and income > max_income:
        max_income = income

    for i in range(len(vouchers)):
        sub_income = income + vouchers[i][1] * (vouchers[i][0] - day)
        sub_vouchers = []
        for j in range(len(vouchers)):
            if (i != j) and ((vouchers[j][0] - day) > 1):
                sub_vouchers.append(vouchers[j])

        solve(sub_vouchers, sub_income, day + 1)


if __name__ == "__main__":
    with open("input1.txt") as f:
        n = int(f.readline().strip())

        vouchers = []

        for i in range(n):
            vouchers.append(
                tuple(map(int, f.readline().split()))
            )

        #print(vouchers)
        solve(vouchers,0 , 0)
        print(max_income)