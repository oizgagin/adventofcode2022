def solution(lists):

    def less(l1, l2):
        if isinstance(l1, int) and isinstance(l2, int):
            return l1 < l2

        if isinstance(l1, int):
            return less([l1], l2)

        if isinstance(l2, int):
            return less(l1, [l2])

        for i in xrange(min(len(l1), len(l2))):
            if less(l1[i], l2[i]):
                return True
            if less(l2[i], l1[i]):
                return False

        return len(l1) < len(l2)

    sum_ = 0
    for i, list_ in enumerate(lists, 1):
        if less(list_[0], list_[1]):
            sum_ += i

    return sum_


def parse(input):
    return map(lambda block: (eval(block[0]), eval(block[1])), map(str.split, input.split("\n\n")))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
