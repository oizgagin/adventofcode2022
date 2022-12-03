def solution(rucksacks):
    priority = lambda type_: ord(type_)-ord('a')+1 if 'a' <= type_ <= 'z' else ord(type_)-ord('A')+27
    return sum(
        priority(list(set(c1) & set(c2))[0])
        for c1, c2 in map(lambda r: (r[:len(r)/2], r[len(r)/2:]), rucksacks)
    )

def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
