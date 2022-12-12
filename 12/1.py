def solution(heightmap):
    spos, epos = (0, 0), (0, 0)

    for i in xrange(len(heightmap)):
        for j in xrange(len(heightmap[i])):
            if heightmap[i][j] == 'S':
                spos = (i, j)
                heightmap[i][j] = 'a'
            if heightmap[i][j] == 'E':
                epos = (i, j)
                heightmap[i][j] = 'z'

    def neighs(p):
        i, j = p
        return [(i+di, j+dj) for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)) if (
            0 <= i+di < len(heightmap) and
            0 <= j+dj < len(heightmap[i]) and
            ord(heightmap[i+di][j+dj]) <= ord(heightmap[i][j])+1
        )]

    q, seen, c = [spos], {spos: True}, 0

    while len(q) > 0:
        c += 1

        q2 = []
        for p in q:
            for n in neighs(p):
                if n == epos:
                    return c

                if n not in seen:
                    seen[n] = True
                    q2.append(n)
        q = q2

    return None


def parse(input):
    return map(lambda line: list(line), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
