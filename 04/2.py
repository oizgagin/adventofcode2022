def solution(assignments):
    overlap_ = lambda p1, p2: p1[0] <= p2[0] <= p1[1] or p2[0] <= p1[0] <= p2[1]
    return len(filter(lambda a: overlap_(*a), assignments))


def parse(input):
    a2p = lambda a: tuple(map(lambda p: tuple(map(int, p.split('-'))), a))
    return map(a2p, map(lambda s: s.split(','), input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
