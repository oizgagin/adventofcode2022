import re


def solution(map_, dirs):

    size = 50

    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3

    dir2drdc = {
        RIGHT: (0, 1),
        DOWN: (1, 0),
        LEFT: (0, -1),
        UP: (-1, 0),
    }

    rotdir = {
        (RIGHT, "L"): UP,
        (RIGHT, "R"): DOWN,
        (DOWN, "L"): RIGHT,
        (DOWN, "R"): LEFT,
        (LEFT, "L"): DOWN,
        (LEFT, "R"): UP,
        (UP, "L"): LEFT,
        (UP, "R"): RIGHT,
    }

    def q(r, c):
        if r < size:
            if size <= c < 2*size:
                return 1
            return 2
        if size <= r < 2*size:
            return 3
        if 2*size <= r < 3*size:
            if c < size:
                return 4
            return 5
        return 6

    r, c, d = 0, map_[0].index("."), RIGHT

    for dir_ in dirs:
        if not isinstance(dir_, int):
            d = rotdir[(d, dir_)]
            continue

        for _ in xrange(dir_):
            dr, dc = dir2drdc[d]
            rr, cc, dd = r + dr, c + dc, d

            if dr > 0:
                if rr == len(map_) or map_[rr][c] == ' ':
                    qq = q(r, c)
                    if qq == 2: # move to 3 from the left
                        rr, cc, dd = c % size + size, 2*size-1, LEFT
                        assert q(rr, cc) == 3
                    elif qq == 5: # move to 6 from the left
                        rr, cc, dd = c % size + 3 * size, size-1, LEFT
                        assert q(rr, cc) == 6
                    elif qq == 6: # move to 2 from the down
                        rr, cc, dd = 0, c + 2 * size, DOWN
                        assert q(rr, cc) == 2

                assert map_[rr][cc] != ' '

                if map_[rr][cc] == '#':
                    break

                r, c, d = rr, cc, dd

            if dr < 0:
                if rr < 0 or map_[rr][c] == ' ':
                    qq = q(r, c)
                    if qq == 1: # move to 6 from right
                        rr, cc, dd = c % size + 3*size, 0, RIGHT
                        assert q(rr, cc) == 6
                    elif qq == 2: # move to 6 from up
                        rr, cc, dd = 4*size-1, c % size, UP
                        assert q(rr, cc) == 6
                    elif qq == 4: # move to 3 from right
                        rr, cc, dd = size + c, size, RIGHT
                        assert q(rr, cc) == 3

                assert map_[rr][cc] != ' '

                if map_[rr][cc] == '#':
                    break

                r, c, d = rr, cc, dd

            if dc > 0:
                if cc == len(map_[r]) or map_[r][cc] == ' ':
                    qq = q(r, c)
                    if qq == 2: # move to 5 from left
                        rr, cc, dd = 3*size-r-1, 2*size-1, LEFT
                        assert q(rr, cc) == 5
                    elif qq == 3: # move to 2 from up
                        rr, cc, dd = size-1, 2*size + r % size, UP
                        assert q(rr, cc) == 2
                    elif qq == 5: # move to 2 from left
                        rr, cc, dd = 3*size-r-1, 3*size-1, LEFT
                        assert q(rr, cc) == 2
                    elif qq == 6: # move to 5 from up
                        rr, cc, dd = 3*size-1, size + r % size, UP
                        assert q(rr, cc) == 5

                assert map_[rr][cc] != ' '

                if map_[rr][cc] == '#':
                    break

                r, c, d = rr, cc, dd

            if dc < 0:
                if cc < 0 or map_[r][cc] == ' ':
                    qq = q(r, c)
                    if qq == 1: # move to 4 from right
                        rr, cc, dd = 3*size-r-1, 0, RIGHT
                        assert q(rr, cc) == 4
                    elif qq == 3: # move to 4 from down
                        rr, cc, dd = 2*size, r%size, DOWN
                        assert q(rr, cc) == 4
                    elif qq == 4: # move to 1 from right
                        rr, cc, dd = 3*size-r-1, size, RIGHT
                        assert q(rr, cc) == 1
                    elif qq == 6: # move to 1 from down
                        rr, cc, dd = 0, size+r%size, DOWN
                        assert q(rr, cc) == 1

                assert map_[rr][cc] != ' '

                if map_[rr][cc] == '#':
                    break

                r, c, d = rr, cc, dd

    return 1000 * (r + 1) + 4 * (c + 1) + d


def parse(input):
    lines = input.splitlines()

    map_ = map(list, lines[:-2])
    maxlen = max(map(lambda s: len(s), map_))
    map_ = map(lambda s: s + [' '] * (maxlen - len(s)), map_)

    dirs = map(lambda s: int(s) if s.isdigit() else s, filter(None, re.split("(\d+|[LR])", lines[-1])))

    return map_, dirs


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
