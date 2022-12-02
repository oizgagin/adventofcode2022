def solution(guide):
    score = lambda hand: {'X': 1, 'Y': 2, 'Z': 3}[hand]

    beats = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    draws = {'A': 'X', 'B': 'Y', 'C': 'Z'}

    outcome = lambda opponent, me: 0 if beats[opponent] == me else 3 if draws[opponent] == me else 6

    return sum(outcome(opponent, me) + score(me) for opponent, me in guide)


def parse(input):
    return map(lambda s: tuple(s.split()), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
