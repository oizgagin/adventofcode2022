import re
from collections import defaultdict


def solution(valves):

    def floyd_warshall():
        dists = defaultdict(lambda: defaultdict(lambda: float('+inf')))

        for v in valves.keys():
            dists[v][v] = 0
            for n in valves[v][1]:
                dists[v][n] = 1

        for i in xrange(len(valves)):
            for v1 in valves.keys():
                for v2 in valves.keys():
                    for v3 in valves.keys():
                        dists[v1][v2] = min(dists[v1][v2], dists[v1][v3] + dists[v3][v2])

        return dists

    dists = floyd_warshall()

    def recurse(valve, released_total, available_valves, closed_valves, counter):
        rate = sum(valves[v][0] for v in available_valves if v not in closed_valves)

        if len(closed_valves) == 0:
            return released_total + counter * rate

        max_ = released_total + rate * counter

        for i, v in enumerate(closed_valves):
            if valves[v][0] == 0 or counter <= dists[valve][v]+1:
                continue

            max_ = max(max_, recurse(
                v,
                released_total + rate * (dists[valve][v] + 1),
                available_valves,
                closed_valves[:i] + closed_valves[i+1:],
                counter - dists[valve][v] - 1
            ))

        return max_

    def subsets(s):
        for i in xrange(1 << len(s)):
            yield set([s[j] for j in xrange(len(s)) if i & (1 << j)])

    closed_valves = set([valve for valve in valves.keys() if valves[valve][0] != 0])

    max_ = 0
    for i, subset in enumerate(subsets(list(closed_valves))):
        max_ = max(max_,
            recurse("AA", 0, tuple(subset), tuple(subset), 26) +
            recurse("AA", 0, tuple(closed_valves - subset), tuple(closed_valves - subset), 26)
        )
    return max_


def parse(input):

    def parse_valve(s):
        m = re.match("Valve (?P<valve>\S+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<valves>.+)", s)
        return m.groupdict()["valve"], (int(m.groupdict()["rate"]), set(m.groupdict()["valves"].split(", ")))

    return dict(map(parse_valve, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
