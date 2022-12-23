from collections import defaultdict, Counter


def solution(scan):
    grid, elves = defaultdict(lambda: defaultdict(int)), []

    for i in xrange(0, len(scan)):
        for j in xrange(0, len(scan[i])):
            if scan[i][j] == "#":
                grid[i][j] = 1
                elves.append((i, j))

    def has_neighs(i, j):
        return any(grid[i+di][j+dj] == 1 for di in (-1, 0, 1) for dj in (-1, 0, 1) if not (di == 0 and dj == 0))

    priorities = [
        ((-1, -1), (-1, 0), (-1, 1)),
        ((1, -1), (1, 0), (1, 1)),
        ((-1, -1), (0, -1), (1, -1)),
        ((-1, 1), (0, 1), (1, 1)),
    ]

    rounds = 0
    while True:
        rounds += 1

        proposes = {}
        for i, j in filter(lambda elf: has_neighs(*elf), elves):
            for priority in priorities:
                if all(grid[i+di][j+dj] == 0 for di, dj in priority):
                    proposes[(i, j)] = (i+priority[1][0], j+priority[1][1])
                    break

        c = Counter(proposes.values())

        moves = 0

        next_ = []
        for elf in elves:
            if elf not in proposes or c[proposes[elf]] > 1:
                next_.append(elf)
                continue

            moves += 1
            next_.append(proposes[elf])
            grid[elf[0]][elf[1]] = 0

        if moves == 0:
            return rounds

        assert len(next_) == len(elves)

        for i, j in next_:
            grid[i][j] = 1

        assert sum(grid[i][j] for i in grid.keys() for j in grid[i].keys()) == len(elves)

        elves = next_
        priorities.append(priorities.pop(0))


def parse(input):
    return map(list, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
