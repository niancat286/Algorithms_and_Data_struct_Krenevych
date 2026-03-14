import sys
min_salary: int = 100500
def solve(matrix: list[list[int]], salary: int):
    global min_salary

    if salary >= min_salary:
        return
    elif len(matrix) == 0:
        min_salary = salary
        return

    for j in range(len(matrix)):
        sub_matrix = [
            row[:j] + row[j+1 :]
            for row in matrix[1:]
        ]
        sub_salary = salary + matrix[0][j]
        solve(sub_matrix,sub_salary)

if __name__ == "__main__":

    f = open("input.txt")
    n =  int(f.readline())
    matrix = [
            [int(num) for num in f.readline().split()]
            for _ in range(n)
        ]
    solve(matrix,0)
    # print(n)
    # print(matrix)
    print(min_salary)
    f.close()