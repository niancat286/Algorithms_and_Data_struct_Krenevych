import sys


def solve():
    data = sys.stdin.read().split()
    if not data: return

    n = int(data[0])
    m = int(data[1])
    bars = list(map(int, data[2:2 + n]))
    plates = list(map(int, data[2 + n:2 + n + m]))

    def get_states(p_list):
        res = {(0, 0)}
        for p in p_list:
            nxt = set()
            for d, s in res:
                nxt.add((d + p, s + p))
                nxt.add((d - p, s))
                nxt.add((d, s))
            res = nxt

        grouped = {}
        for d, s in res:
            if d not in grouped: grouped[d] = set()
            grouped[d].add(s)
        return grouped

    mid = m // 2
    p1 = get_states(plates[:mid])
    p2 = get_states(plates[mid:])

    possible_x = set()
    for d1, s1_set in p1.items():
        if -d1 in p2:
            for s1 in s1_set:
                for s2 in p2[-d1]:
                    possible_x.add(s1 + s2)

    ans = set()
    for b in bars:
        for x in possible_x:
            ans.add(b + 2 * x)

    for r in sorted(ans):
        print(r)


if __name__ == "__main__":
    solve()