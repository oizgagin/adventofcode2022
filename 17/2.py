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

    minx, maxx, ji = 0, 6, 0

    i, seen, curr, currs = 1, dict(), [-1] * (maxx - minx + 1), []
    repeati, repeatdiff, repeatcurr = None, None, None

    while True:
        shape = move(shapes[(i-1) % len(shapes)], 2, max(curr)+4)

        startji = ji

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
            curr[c[0]] = max(curr[c[0]], c[1])

        currs.append(curr[:])

        diff = tuple([tuple(curr[j] - curr[j-1] for j in xrange(minx+1, maxx+1)), (i-1) % len(shapes), startji % len(jets)])
        if diff not in seen:
            seen[diff] = {
                "round": i,
                "curr": curr[:],
            }
        else:
            repeati, repeatdiff, repeatcurr = i, diff, curr
            break

        i += 1

    rounds = 1000000000000

    rounds -= seen[repeatdiff]["round"]

    cycle_len = repeati - seen[repeatdiff]["round"]
    cycles, left = rounds / cycle_len, rounds % cycle_len

    dx1 = [repeatcurr[i] - seen[repeatdiff]["curr"][i] for i in xrange(minx, maxx+1)]

    xs = currs[seen[repeatdiff]["round"]-1][:]

    for i in xrange(minx, maxx+1):
        xs[i] += cycles * dx1[i]

    first = seen[repeatdiff]["round"]
    dx2 = [currs[first+left-1][i] - currs[first-1][i] for i in xrange(minx, maxx+1)]
    for i in xrange(minx, maxx+1):
        xs[i] += dx2[i]

    return max(xs)+1


def parse(input):
    return list(input.strip())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
