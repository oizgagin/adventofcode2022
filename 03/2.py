def solution(rucksacks):
    priority = lambda type_: ord(type_)-ord('a')+1 if 'a' <= type_ <= 'z' else ord(type_)-ord('A')+27
    return sum(
        priority(list(set(g1) & set(g2) & set(g3))[0])
        for g1, g2, g3 in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
    )

def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
