from collections import defaultdict


def solution(jets):

    shapes = [
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (0, 1), (1, 0), (1, 1)),
    ]

    def move(p, dx, dy):
        return tuple((c[0]+dx, c[1]+dy) for c in p)

    jet2dx = lambda jet: -1 if jet == '<' else 1

    grid = defaultdict(lambda: defaultdict(int))

    minx, maxx, maxy, ji = 0, 6, -1, 0
    for i in xrange(0, 2022):
        shape = move(shapes[i % len(shapes)], 2, maxy+4)

        while True:
            dx = jet2dx(jets[ji % len(jets)])

            shape = move(shape, dx, 0)
            if any(c[0] < minx or c[0] > maxx for c in shape) or any(grid[c[0]][c[1]] == 1 for c in shape):
                shape = move(shape, -dx, 0)

            ji += 1

            shape = move(shape, 0, -1)
            if any([
                any(c[0] < minx or c[0] > maxx for c in shape),
                any(c[1] < 0 for c in shape),
                any(grid[c[0]][c[1]] == 1 for c in shape),
            ]):
                shape = move(shape, 0, 1)
                break

        for c in shape:
            grid[c[0]][c[1]] = 1

        maxy = max(maxy, max(c[1] for c in shape))

    return maxy+1


def parse(input):
    return list(input.strip())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
