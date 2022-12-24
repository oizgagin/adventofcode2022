def solution(map_):

    def move_blizzards(ups, downs, lefts, rights):
        def move(p, dr, dc):
            r, c = p[0]+dr, p[1]+dc
            if r == 0: r = len(map_)-2
            if r == len(map_)-1: r = 1
            if c == 0: c = len(map_[r])-2
            if c == len(map_[r])-1: c = 1
            return (r, c)

        ups2 = set(map(lambda p: move(p, -1, 0), ups))
        downs2 = set(map(lambda p: move(p, 1, 0), downs))
        lefts2 = set(map(lambda p: move(p, 0, -1), lefts))
        rights2 = set(map(lambda p: move(p, 0, 1), rights))

        assert len(ups) == len(ups2)
        assert len(downs) == len(downs2)
        assert len(lefts) == len(lefts2)
        assert len(rights) == len(rights2)

        assert ups != ups2
        assert downs != downs2
        assert lefts != lefts2
        assert rights != rights2

        return ups2, downs2, lefts2, rights2

    start, dest = (0, 1), (len(map_)-1, len(map_[-1])-2)

    def neighbours(p):
        r, c = p

        res = set([p])

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if c == 1:
                if not (r+dr < 0 or r+dr >= len(map_)-1):
                    res.add((r+dr, c+dc))
                continue

            if c == len(map_[0])-2:
                if not (r+dr < 1 or r+dr >= len(map_)):
                    res.add((r+dr, c+dc))
                continue

            if r+dr < 1 or r+dr >= len(map_)-1:
                continue

            if c+dc < 1 or c+dc >= len(map_[0])-1:
                continue

            res.add((r+dr, c+dc))

        return res

    ups = set([(i, j) for i in xrange(len(map_)) for j in xrange(len(map_[i])) if map_[i][j] == "^"])
    downs = set([(i, j) for i in xrange(len(map_)) for j in xrange(len(map_[i])) if map_[i][j] == "v"])
    lefts = set([(i, j) for i in xrange(len(map_)) for j in xrange(len(map_[i])) if map_[i][j] == "<"])
    rights = set([(i, j) for i in xrange(len(map_)) for j in xrange(len(map_[i])) if map_[i][j] == ">"])

    q = [start]

    minutes = 0

    while dest not in q:
        minutes += 1

        ups, downs, lefts, rights = move_blizzards(ups, downs, lefts, rights)

        q2 = set()
        for p in q:
            for n in neighbours(p):
                if n not in ups and n not in downs and n not in lefts and n not in rights:
                    q2.add(n)

        q = q2


    q = [dest]
    while start not in q:
        minutes += 1

        ups, downs, lefts, rights = move_blizzards(ups, downs, lefts, rights)

        q2 = set()
        for p in q:
            for n in neighbours(p):
                if n not in ups and n not in downs and n not in lefts and n not in rights:
                    q2.add(n)

        q = q2

    q = [start]
    while dest not in q:
        minutes += 1

        ups, downs, lefts, rights = move_blizzards(ups, downs, lefts, rights)

        q2 = set()
        for p in q:
            for n in neighbours(p):
                if n not in ups and n not in downs and n not in lefts and n not in rights:
                    q2.add(n)

        q = q2

    return minutes


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
