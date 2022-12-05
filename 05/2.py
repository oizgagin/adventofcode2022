import re
from collections import defaultdict


def solution(stacks, moves):
    def move(from_, to, num):
        stacks[to].extend(stacks[from_][-num:])
        stacks[from_] = stacks[from_][:-num]

    for m in moves:
        move(*m)

    return ''.join(stacks[id_][-1] if stacks[id_] else '' for id_ in sorted(stacks.keys(), key=int))


def parse(input):
    ss, ms = map(str.splitlines, input.split("\n\n"))

    pos2stack = {}
    for pos, stack in enumerate(ss[-1]):
        if stack.isdigit():
            pos2stack[pos] = stack

    stacks = defaultdict(list)
    for line in ss[:-1]:
        for pos, ch in enumerate(line):
            if ch.isalpha():
                stacks[pos2stack[pos]].insert(0, ch)

    moves = []
    for m in ms:
        match = re.match("move (?P<num>\d+) from (?P<from>\d) to (?P<to>\d)", m).groupdict()
        moves.append((match["from"], match["to"], int(match["num"])))

    return stacks, moves


def main():
    input = open("input", "r").read()
    print(solution(*parse(input)))


main()
