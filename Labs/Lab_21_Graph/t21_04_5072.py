if __name__ == "__main__":
    with open("input.txt") as f:
        n = int(f.readline().strip())

        count = 0
        for _ in range(n):
            count += sum(list(map(int, f.readline().split())))

        print(count)