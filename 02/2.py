def solution(guide):
    outcomes = lambda outcome: {'X': 0, 'Y': 3, 'Z': 6}[outcome]
    score = lambda hand: {'X': 1, 'Y': 2, 'Z': 3}[hand]

    me = lambda opponent, outcome: {
        'X': {
            'A': 'Z',
            'B': 'X',
            'C': 'Y',
        },
        'Y': {
            'A': 'X',
            'B': 'Y',
            'C': 'Z',
        },
        'Z': {
            'A': 'Y',
            'B': 'Z',
            'C': 'X',
        },
    }[outcome][opponent]

    return sum(score(me(opponent, outcome)) + outcomes(outcome) for opponent, outcome in guide)


def parse(input):
    return map(lambda s: tuple(s.split()), input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
