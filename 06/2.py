def solution(datastream):
    return filter(
        lambda t: len(set(t[1])) == len(t[1]),
        enumerate(zip(*(datastream[i:] for i in xrange(0, 14))))
    )[0][0] + 14


def parse(input):
    return input.strip()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
