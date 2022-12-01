def solution(elfcalories):
    return sum(sorted(map(sum, elfcalories), reverse=True)[:3])


def parse(input):
    return [map(int, block.splitlines()) for block in input.split("\n\n")]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
