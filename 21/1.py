def solution(monkeys):

    evals = {}

    def eval_(monkey):
        if isinstance(monkeys[monkey], int):
            return monkeys[monkey]

        v = eval("%s %s %s" % (eval_(monkeys[monkey][0]), monkeys[monkey][1], eval_(monkeys[monkey][2])))
        evals[monkey] = v
        return v

    return eval_("root")


def parse(input):
    parse_deps = lambda s: int(s) if s.isdigit() else tuple(s.split(' '))
    return dict((line.split(":")[0], parse_deps(line.split(":")[1].strip())) for line in input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
