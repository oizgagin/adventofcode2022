def solution(commands):
    cycles, x = 0, 1

    sum_ = 0

    for cmd in commands:
        if cmd[0] == 'noop':
            cycles += 1

            if cycles % 40 == 20:
                sum_ += cycles * x

        if cmd[0] == 'addx':
            cycles += 1
            if cycles % 40 == 20:
                sum_ += cycles * x

            cycles += 1
            if cycles % 40 == 20:
                sum_ += cycles * x

            x += cmd[1]

    return sum_


def parse(input):
    return map(lambda ss: (ss[0], int(ss[1]) if len(ss) > 1 else None), map(str.split, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
