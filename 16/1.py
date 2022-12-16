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

    def recurse(valve, released_total, closed_valves, counter):
        rate = sum(valves[v][0] for v in valves.keys() if v not in closed_valves)

        if all(valves[v][0] == 0 for v in closed_valves):
            return released_total + counter * rate

        max_ = released_total + rate * counter

        for i, v in enumerate(closed_valves):
            if valves[v][0] == 0 or counter <= dists[valve][v]+1:
                continue

            max_ = max(max_, recurse(
                v,
                released_total + rate * (dists[valve][v] + 1),
                closed_valves[:i] + closed_valves[i+1:],
                counter - dists[valve][v] - 1
            ))

        return max_

    return recurse("AA", 0, tuple(valves.keys()), 30)


def parse(input):

    def parse_valve(s):
        m = re.match("Valve (?P<valve>\S+) has flow rate=(?P<rate>\d+); tunnels? leads? to valves? (?P<valves>.+)", s)
        return m.groupdict()["valve"], (int(m.groupdict()["rate"]), set(m.groupdict()["valves"].split(", ")))

    return dict(map(parse_valve, input.splitlines()))


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
