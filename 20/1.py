def solution(file):
    list_ = list(enumerate(file))
    dict_ = dict(enumerate(list_))

    for i, t in sorted(dict_.iteritems()):
        pos = list_.index(t)

        step = -1 if t[1] < 0 else 1
        for i in xrange(0, t[1], step):
            next_pos = (pos + step) % len(list_)
            list_[pos], list_[next_pos] = list_[next_pos], list_[pos]
            pos = next_pos

    pos = list_.index(filter(lambda t: t[1] == 0, list_)[0])

    return (
        list_[(pos + (1000 % len(list_))) % len(list_)][1] +
        list_[(pos + (2000 % len(list_))) % len(list_)][1] +
        list_[(pos + (3000 % len(list_))) % len(list_)][1]
    )


def parse(input):
    return map(int, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
