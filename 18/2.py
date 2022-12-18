import sys
sys.setrecursionlimit(100 * 1000)


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

    maxx, maxy, maxz =  max(map(lambda c: c[0], cubes))+1, max(map(lambda c: c[1], cubes))+1, max(map(lambda c: c[2], cubes))+1

    cubeset, outside = set(cubes), set()

    def dfs(p):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    if len(filter(None, [dx, dy, dz])) != 1: continue

                    x, y, z = p[0] + dx, p[1] + dy, p[2] + dz

                    if any([
                        x < 0,
                        x > maxx,
                        y < 0,
                        y > maxy,
                        z < 0,
                        z > maxz,
                        (x, y, z) in cubeset,
                        (x, y, z) in outside,
                    ]):
                        continue

                    outside.add((x, y, z))

                    dfs((x, y, z))

    dfs((0, 0, 0))

    inside = 0

    for x in xrange(0, maxx+1):
        for y in xrange(0, maxy+1):
            for z in xrange(0, maxz+1):
                if (x, y, z) in cubeset or (x, y, z) in outside: continue

                adjs = 0
                for cube in cubes:
                    if dist(cube, (x, y, z)) == 1:
                        adjs += 1

                inside += adjs

    return total - inside


def parse(input):
    return map(lambda s: tuple(map(int, s.split(","))), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
