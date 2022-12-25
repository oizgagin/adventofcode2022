import math


def solution(snafus):
    maxlen = max(len(snafu) for snafu in snafus)

    digits = {
        "0": 0,
        "1": 1,
        "2": 2,
        "-": -1,
        "=": -2,
    }

    snafus = map(lambda snafu: map(lambda ch: digits[ch], list(reversed("0" * (maxlen - len(snafu)) + snafu))), snafus)

    res, carry = [], 0
    for i in xrange(0, maxlen):
        sum_ = sum(snafu[i] for snafu in snafus) + carry

        if sum_ >= 0:
            carry, mod = sum_ / 5, sum_ % 5
            if mod == 3:
                res.append(-2)
                carry += 1
            elif mod == 4:
                res.append(-1)
                carry += 1
            else:
                res.append(mod)

        if sum_ < 0:
            carry, mod = (sum_ + 2) / 5, sum_ % 5
            if mod == 4:
                res.append(-1)
            elif mod == 3:
                res.append(-2)
            else:
                res.append(mod)

    revdigits = {
        0: "0",
        1: "1",
        2: "2",
        -1: "-",
        -2: "=",
    }

    res = ''.join(reversed(map(lambda d: revdigits[d], res)))
    return res


def parse(input):
    return input.splitlines()


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
