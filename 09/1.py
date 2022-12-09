from collections import defaultdict


def solution(dirs):
    grid = defaultdict(lambda: defaultdict(int))

    add = lambda t1, t2: (t1[0]+t2[0], t1[1]+t2[1])

    dd = { 'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0) }

    sign = lambda x: -1 if x < 0 else 1 if x > 0 else 0

    def move(t, h):
        if t[0] == h[0] and abs(t[1] - h[1]) == 2:
            return (t[0], (t[1] + h[1])/2)
        if t[1] == h[1] and abs(t[0] - h[0]) == 2:
            return ((t[0] + h[0])/2, t[1])
        if abs(t[0] - h[0]) == 2 or abs(t[1] - h[1]) == 2:
            return (t[0] + sign(h[0]-t[0]), t[1] + sign(h[1]-t[1]))
        return t

    H, T = (0, 0), (0, 0)

    for d, c in dirs:
        for _ in xrange(c):
            H = add(H, dd[d])
            T = move(T, H)
            grid[T[0]][T[1]] += 1

    res = 0
    for i in grid.keys():
        for j in grid[i].keys():
            if grid[i][j] >= 1:
                res += 1
    return res


def parse(input):
    return map(lambda s: (s.split()[0], int(s.split()[1])), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
