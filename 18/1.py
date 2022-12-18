def solution(cubes):

    dist = lambda c1, c2: sum(abs(c1[i] - c2[i]) for i in xrange(3))

    total = 0

    for c1 in cubes:
        adjs = 0

        for c2 in cubes:
            if c1 == c2: continue

            if dist(c1, c2) == 1:
                adjs += 1

        total += 6 - adjs

    return total


def parse(input):
    return map(lambda s: tuple(map(int, s.split(","))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
