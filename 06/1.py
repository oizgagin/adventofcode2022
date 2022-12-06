def solution(datastream):
    return filter(
        lambda t: len(set(t[1])) == len(t[1]),
        enumerate(zip(datastream[:], datastream[1:], datastream[2:], datastream[3:]))
    )[0][0] + 4


def parse(input):
    return input.strip()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
