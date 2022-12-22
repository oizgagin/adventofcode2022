import re


def solution(map_, dirs):

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

    up, down, left, right = [0]*len(map_[0]), [0]*len(map_[0]), [0]*len(map_), [0]*len(map_)

    for row in xrange(0, len(map_)):
        for col in xrange(0, len(map_[row])):
            if map_[row][col] != ' ':
                left[row] = col
                break

    for row in xrange(0, len(map_)):
        for col in xrange(len(map_[row])-1, -1, -1):
            if map_[row][col] != ' ':
                right[row] = col
                break

    for col in xrange(0, len(map_[0])):
        for row in xrange(0, len(map_)):
            if map_[row][col] != ' ':
                up[col] = row
                break

    for col in xrange(0, len(map_[0])):
        for row in xrange(len(map_)-1, -1, -1):
            if map_[row][col] != ' ':
                down[col] = row
                break

    r, c, d = 0, map_[0].index("."), RIGHT

    for dir_ in dirs:
        if not isinstance(dir_, int):
            d = rotdir[(d, dir_)]
            continue

        for _ in xrange(dir_):
            dr, dc = dir2drdc[d]
            rr, cc = r + dr, c + dc

            if dr > 0:
                if rr == len(map_) or map_[rr][c] == ' ':
                    rr = up[c]
                if map_[rr][c] == '#':
                    break
                r = rr

            if dr < 0:
                if rr < 0 or map_[rr][c] == ' ':
                    rr = down[c]
                if map_[rr][c] == '#':
                    break
                r = rr

            if dc > 0:
                if cc == len(map_[r]) or map_[r][cc] == ' ':
                    cc = left[r]
                if map_[r][cc] == '#':
                    break
                c = cc

            if dc < 0:
                if cc < 0 or map_[r][cc] == ' ':
                    cc = right[r]
                if map_[r][cc] == '#':
                    break
                c = cc

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
