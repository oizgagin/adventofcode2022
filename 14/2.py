from collections import defaultdict


def solution(lines):
    grid = defaultdict(lambda: defaultdict(int))

    for line in lines:
        for p1, p2 in zip(line, line[1:]):
            x1, y1 = p1
            x2, y2 = p2

            for x in xrange(min(x1, x2), max(x1, x2)+1):
                for y in xrange(min(y1, y2), max(y1, y2)+1):
                    grid[x][-y] = 1

    miny = min(min(ys) for ys in grid.values())-2

    get = lambda x, y: 1 if y == miny else grid[x][y]

    def round_():
        sandx, sandy = 500, 1

        while True:
            if get(sandx, sandy-1) == 1 and get(sandx-1, sandy-1) == 1 and get(sandx+1, sandy-1) == 1:
                grid[sandx][sandy] = 1
                return

            if get(sandx, sandy-1) == 1 and get(sandx-1, sandy-1) == 0:
                sandx -= 1
                continue

            if get(sandx, sandy-1) == 1 and get(sandx+1, sandy-1) == 0:
                sandx += 1
                continue

            sandy -= 1

    steps = 0
    while grid[500][0] == 0:
        round_()
        steps += 1

    return steps


def parse(input):
    lines = []

    for line in input.splitlines():
        points = []
        for point in line.split(" -> "):
            points.append(tuple(map(int, point.split(","))))
        lines.append(points)

    return lines


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
