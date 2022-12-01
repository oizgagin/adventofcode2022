def solution(elfcalories):
    return max(map(sum, elfcalories))


def parse(input):
    return [map(int, block.splitlines()) for block in input.split("\n\n")]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
