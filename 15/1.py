import re
from collections import defaultdict


def solution(sb):
    dist = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    squares = []

    for s, b in sb:
        d = dist(s, b)

        squares.append((
            (s[0] - d, s[1]),
            (s[0] + d, s[1]),
            (s[0], s[1] - d),
            (s[0], s[1] + d),
        ))

    y = 2000000

    segments = []

    for square in squares:
        xs, ys = map(lambda p: p[0], square), map(lambda p: p[1], square)
        if y < min(ys) or y > max(ys):
            continue

        ips = set()

        for p1, p2 in ((p1, p2) for p1 in square for p2 in square):
            if p1[0] == p2[0] or p1[1] == p2[1] or y < min(p1[1], p2[1]) or y > max(p1[1], p2[1]):
                continue

            a1, b1 = p2[1]-p1[1], p1[0]-p2[0]
            c1 = a1*p1[0] + b1*p1[1]

            p1x, p1y, p2x, p2y = min(xs), y, max(xs), y

            a2, b2 = p2y-p1y, p1x-p2x
            c2 = a2*p1x + b2*p1y

            det = a1*b2 - a2*b1

            ix, iy = (b2*c1 - b1*c2)/det, (a1*c2 - a2*c1)/det

            ips.add(ix)

        if len(ips) == 0:
            continue
        elif len(ips) == 1:
            segments.append((list(ips)[0], list(ips)[0]))
        else:
            segments.append(tuple(sorted(ips)))

    segments.sort(key=lambda t: t[0])

    intervals = []

    l, r = segments[0]
    for seg in segments[1:]:
        if seg[0] <= r:
            r = max(r, seg[1])
        else:
            intervals.append((l, r))
            l, r = seg

    intervals.append((l, r))

    ss, bs = set(s for s, _ in sb), set(b for _, b in sb)

    res = 0
    for interval in intervals:
        res += interval[1] - interval[0] + 1
        for s in ss:
            if s[1] == y and interval[0] <= s[0] <= interval[1]:
                res -= 1
        for b in bs:
            if b[1] == y and interval[0] <= b[0] <= interval[1]:
                res -= 1

    return res


def parse(input):
    parse_coords = lambda s: tuple(map(int, re.match("x=(?P<x>\-?\d+), y=(?P<y>\-?\d+)", s).groups()))

    sb = []
    for line in input.splitlines():
        s, b = line.split(":")[0][len("Sensor at "):], line.split(":")[1][len(" closest beacon is at "):]
        sb.append((parse_coords(s), parse_coords(b)))
    return sb


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
