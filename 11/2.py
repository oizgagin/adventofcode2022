def solution(monkeys):
    inspections = [0] * len(monkeys)

    mod = reduce(lambda acc, x: acc * x, map(lambda monkey: monkey[3], monkeys), 1)

    for _ in xrange(10000):
        for i, monkey in enumerate(monkeys):
            while len(monkey[1]) > 0:
                item = monkey[1].pop(0)
                new_worry = eval(monkey[2].replace('old', str(item))) % mod
                if new_worry % monkey[3] == 0:
                    monkeys[monkey[4]][1].append(new_worry)
                else:
                    monkeys[monkey[5]][1].append(new_worry)

                inspections[i] += 1

    return reduce(lambda acc, x: acc * x, sorted(inspections, reverse=True)[:2], 1)


def parse(input):

    def parse_monkey(descr):
        lines = descr.splitlines()

        id_ = int(lines[0].strip(": ")[len("Monkey "):])
        items = map(int, lines[1].strip()[len("Starting items: "):].split(", "))
        operation = lines[2].strip()[len("Operation: new = "):]
        test = int(lines[3].strip()[len("Test: divisible by "):])
        test_true = int(lines[4].strip()[len("If true: throw to monkey "):])
        test_false = int(lines[5].strip()[len("If false: throw to monkey "):])

        return (id_, items, operation, test, test_true, test_false)


    return map(parse_monkey, input.split("\n\n"))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
