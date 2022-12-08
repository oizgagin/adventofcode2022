def solution(trees):
    n, m = len(trees), len(trees[0])

    def mkarray():
        return [[0] * m for _ in xrange(n)]

    left, right, top, bottom = mkarray(), mkarray(), mkarray(), mkarray()

    for i in xrange(n):
        for j in xrange(m):
            left[i][j] = trees[i][j] if j == 0 else max(trees[i][j], left[i][j-1])

    for i in xrange(n):
        for j in xrange(m-1, -1, -1):
            right[i][j] = trees[i][j] if j == m-1 else max(trees[i][j], right[i][j+1])

    for j in xrange(m):
        for i in xrange(n):
            top[i][j] = trees[i][j] if i == 0 else max(trees[i][j], top[i-1][j])

    for j in xrange(m):
        for i in xrange(n-1, -1, -1):
            bottom[i][j] = trees[i][j] if i == n-1 else max(trees[i][j], bottom[i+1][j])

    res = (m + n) * 2 - 4
    for i in xrange(1, n-1):
        for j in xrange(1, m-1):
            if any([
                trees[i][j] > left[i][j-1],
                trees[i][j] > right[i][j+1],
                trees[i][j] > top[i-1][j],
                trees[i][j] > bottom[i+1][j],
            ]):
                res += 1

    return res


def parse(input):
    return [map(int, list(line)) for line in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
