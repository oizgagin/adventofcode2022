def solution(lists):

    lists.extend([[[2]], [[6]]])

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

    def cmp(l1, l2):
        if less(l1, l2):
            return 1
        if less(l2, l1):
            return -1
        return 0

    lists.sort(cmp=cmp, reverse=True)

    res = 1
    for i, l in enumerate(lists, 1):
        if l == [[2]] or l == [[6]]:
            res *= i
    return res


def parse(input):
    return map(eval, filter(None, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
