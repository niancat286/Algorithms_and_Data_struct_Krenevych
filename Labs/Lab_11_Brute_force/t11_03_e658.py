


DRAW = 0
FIRST = 1
SECOND = 2


XX = "X"
OO = "O"

k: int


def solve(state: str, turn: int) -> int:
    #print(state, turn)
    i = -1

    while True:
        i = state.find(OO, i+1)

        if i == -1:
            break

        sub_state = state[:i] + XX + state[i+k:]
        sub_turn = FIRST if turn == SECOND else SECOND
        if solve(sub_state, sub_turn) == turn:
            return turn



    return FIRST if turn == SECOND else SECOND



if __name__ == "__main__":
    with open("input.txt") as f:

        n, k = map(int, f.readline().split())
        state = f.readline()

        XX *= k
        OO *= k

        if state.find(OO) == -1:
            print(DRAW)
        else:
            print(solve(state, FIRST))
