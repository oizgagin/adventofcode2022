from collections import defaultdict


def solution(dirs):
    sizes = defaultdict(int)

    def recurse(dir_):
        sizes[dir_] = sum(item[2] if item[0] == "file" else recurse(item[1]) for item in dirs[dir_])
        return sizes[dir_]

    recurse("")

    return sum(size if size <= 100000 else 0 for size in sizes.values())


def parse(input):
    lines = iter(input.splitlines())

    path, dirs = [], defaultdict(lambda: [])

    def make_path(dir_=None):
        return "/".join(path + [dir_] if dir_ is not None else path)

    def parse_ls():
        wd = make_path()

        for line in lines:
            if line.startswith("$"):
                parse_command(line)
            elif line.startswith("dir"):
                dirs[wd].append(("dir", make_path(line.split()[1])))
            else:
                dirs[wd].append(("file", make_path(line.split()[1]), int(line.split()[0])))

    def parse_command(cmd):
        name, args = cmd.split()[1], cmd.split()[2:]
        if name == "cd" and args[0] == "..":
            path.pop()
        elif name == "cd":
            path.append("" if args[0] == "/" else args[0])
        elif name == "ls":
            parse_ls()

    for line in lines:
        parse_command(line)

    return dirs


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
