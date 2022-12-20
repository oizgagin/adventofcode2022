import re


def solution(blueprints):

    def recurse_with_memo(blueprint, minutes):

        memo = {}

        max_ores = max([
            blueprint["ore_robot_ores"],
            blueprint["clay_robot_ores"],
            blueprint["obsidian_robot_ores"],
            blueprint["geode_robot_ores"],
        ])

        def recurse(
            ore_robots, ore_total,
            clay_robots, clay_total,
            obsidian_robots, obsidian_total,
            geode_robots, geode_total,
            minutes,
        ):
            if minutes <= 0:
                return geode_total

            if (
                (geode_robots == 0 and minutes == 1) or
                (obsidian_robots == 0 and minutes == 2) or
                (clay_robots == 0 and minutes == 3)
            ):
                return 0

            k = (
                ore_robots, ore_total,
                clay_robots, clay_total,
                obsidian_robots, obsidian_total,
                geode_robots, geode_total,
                minutes
            )

            if k in memo:
                return memo[k]

            can_build_ore = ore_total >= blueprint["ore_robot_ores"]
            can_build_clay = ore_total >= blueprint["clay_robot_ores"]
            can_build_obsidian = (
                ore_total >= blueprint["obsidian_robot_ores"] and clay_total >= blueprint["obsidian_robot_clays"]
            )
            can_build_geode = (
                ore_total >= blueprint["geode_robot_ores"] and obsidian_total >= blueprint["geode_robot_obsidians"]
            )

            max_ = geode_total + minutes * geode_robots

            if can_build_geode:
                max_ = max(max_, recurse(
                    ore_robots, ore_total + ore_robots - blueprint["geode_robot_ores"],
                    clay_robots, clay_total + clay_robots,
                    obsidian_robots, obsidian_total + obsidian_robots - blueprint["geode_robot_obsidians"],
                    geode_robots+1, geode_total + geode_robots,
                    minutes-1,
                ))
                memo[k] = max_
                return max_

            if (
                can_build_obsidian and
                obsidian_robots+1 <= blueprint["geode_robot_obsidians"] and
                minutes > 1
            ):
                max_ = max(max_, recurse(
                    ore_robots, ore_total + ore_robots - blueprint["obsidian_robot_ores"],
                    clay_robots, clay_total + clay_robots - blueprint["obsidian_robot_clays"],
                    obsidian_robots+1, obsidian_total + obsidian_robots,
                    geode_robots, geode_total + geode_robots,
                    minutes-1,
                ))

            if (
                can_build_clay and
                clay_robots+1 <= blueprint["obsidian_robot_clays"] and
                minutes > 2
            ):
                max_ = max(max_, recurse(
                    ore_robots, ore_total + ore_robots - blueprint["clay_robot_ores"],
                    clay_robots+1, clay_total + clay_robots,
                    obsidian_robots, obsidian_total + obsidian_robots,
                    geode_robots, geode_total + geode_robots,
                    minutes-1,
                ))

            if can_build_ore and ore_robots+1 <= max_ores:
                max_ = max(max_, recurse(
                    ore_robots+1, ore_total + ore_robots - blueprint["ore_robot_ores"],
                    clay_robots, clay_total + clay_robots,
                    obsidian_robots, obsidian_total + obsidian_robots,
                    geode_robots, geode_total + geode_robots,
                    minutes-1,
                ))

            max_ = max(max_, recurse(
                ore_robots, ore_total + ore_robots,
                clay_robots, clay_total + clay_robots,
                obsidian_robots, obsidian_total + obsidian_robots,
                geode_robots, geode_total + geode_robots,
                minutes-1,
            ))

            memo[k] = max_
            return max_

        return recurse(
            1, 0,
            0, 0,
            0, 0,
            0, 0,
            minutes
        )

    return (
        recurse_with_memo(blueprints[0], 32) *
        recurse_with_memo(blueprints[1], 32) *
        recurse_with_memo(blueprints[2], 32)
    )


def parse(input):

    def parse_blueprint(s):
        return dict(map(lambda t: (t[0], int(t[1])), re.match(
            "Blueprint (?P<blueprint>\d+): " +
            "Each ore robot costs (?P<ore_robot_ores>\d+) ore\. " +
            "Each clay robot costs (?P<clay_robot_ores>\d+) ore\. " +
            "Each obsidian robot costs (?P<obsidian_robot_ores>\d+) ore and (?P<obsidian_robot_clays>\d+) clay\. " +
            "Each geode robot costs (?P<geode_robot_ores>\d+) ore and (?P<geode_robot_obsidians>\d+) obsidian\.",
        s).groupdict().iteritems()))

    return map(parse_blueprint, input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
