def solution(commands):
    cycles, x = 0, 1

    crt = [[0] * 40 for _ in xrange(6)]

    def pprint():
        print '\n'.join(''.join(map(lambda p: '#' if p else '.', row)) for row in crt)

    pos = 0

    def cb():
        row, col = pos / 40, pos % 40
        if x-1 <= col <= x+1:
            crt[row][col] = 1

    for cmd in commands:
        if cmd[0] == 'noop':
            cycles += 1
            cb(); pos += 1

        if cmd[0] == 'addx':
            cycles += 1
            cb(); pos += 1
            cycles += 1
            cb(); pos += 1
            x += cmd[1]

    pprint()

    return


def parse(input):
    return map(lambda ss: (ss[0], int(ss[1]) if len(ss) > 1 else None), map(str.split, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
