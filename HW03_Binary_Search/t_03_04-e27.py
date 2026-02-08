def find_max(n):
    if n == 0: return 0

    L = n.bit_length()

    max_val = n
    current = n

    limit = (1 << L) - 1

    for i in range(L - 1):
        current = ((current << 1) | (current >> (L - 1))) & limit
        if current > max_val:
            max_val = current

    return max_val


if __name__ == "__main__":
    n = int(input())
    print(find_max(n))