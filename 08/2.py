def solution(trees):
    n, m = len(trees), len(trees[0])

    max_ = 0
    for i in xrange(n):
        for j in xrange(m):
            top = 0
            for ii in xrange(i-1, -1, -1):
                top += 1
                if trees[ii][j] >= trees[i][j]:
                    break

            bottom = 0
            for ii in xrange(i+1, n):
                bottom += 1
                if trees[ii][j] >= trees[i][j]:
                    break

            left = 0
            for jj in xrange(j-1, -1, -1):
                left += 1
                if trees[i][jj] >= trees[i][j]:
                    break

            right = 0
            for jj in xrange(j+1, m):
                right += 1
                if trees[i][jj] >= trees[i][j]:
                    break

            v = top * bottom * left * right

            max_ = max(v, max_)

    return max_


def parse(input):
    return [map(int, list(line)) for line in input.splitlines()]


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
