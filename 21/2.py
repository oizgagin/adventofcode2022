def solution(monkeys):

    has_humn = {}

    def has(monkey):
        if monkey == "humn":
            has_humn[monkey] = True
            return True
        if isinstance(monkeys[monkey], int):
            has_humn[monkey] = False
            return False

        l, r = has(monkeys[monkey][0]), has(monkeys[monkey][2])
        has_humn[monkey] = l or r
        return l or r

    has("root")

    def eval_(monkey):
        if isinstance(monkeys[monkey], int):
            return monkeys[monkey]
        return eval("%s %s %s" % (eval_(monkeys[monkey][0]), monkeys[monkey][1], eval_(monkeys[monkey][2])))

    collapsed = {}

    def recurse(monkey):
        if monkey == "humn":
            collapsed[monkey] = None
            return "humn"

        if not has_humn[monkey]:
            collapsed[monkey] = eval_(monkey)
            return collapsed[monkey]

        l, op, r = monkeys[monkey]
        collapsed[monkey] = (recurse(l), op, recurse(r))
        return monkey

    recurse("root")

    def flat(monkey, curr):
        l, op, r = collapsed[monkey]

        # humn op r = curr
        if l == "humn":
            if op == "+":
                return "((%s)-%s))" % (curr, r)
            if op == "-":
                return "((%s)+%s)" % (curr, r)
            if op == "*":
                return "((%s)/%s)" % (curr, r)
            if op == "/":
                return "((%s)*%s)" % (curr, r)

        # l op humn = curr
        if r == "humn":
            if op == "+":
                return "((%s)-%s)" % (curr, l)
            if op == "-":
                return "(%s-(%s))" % (l, curr)
            if op == "*":
                return "((%s)/%s)" % (curr, r)
            if op == "/":
                return "(%s/(%s))" % (l, curr)

        # int op r = curr
        if isinstance(l, int):
            if op == "+":
                return flat(r, "((%s)-%s)" % (curr, l))
            if op == "-":
                return flat(r, "(%s-(%s))" % (l, curr))
            if op == "*":
                return flat(r, "((%s)/%s)" % (curr, l))
            if op == "/":
                return flat(r, "(%s/(%s))" % (l, curr))

        # l op int = curr
        if isinstance(r, int):
            if op == "+":
                return flat(l, "((%s)-%s)" % (curr, r))
            if op == "-":
                return flat(l, "((%s)+%s)" % (curr, r))
            if op == "*":
                return flat(l, "((%s)/%s)" % (curr, r))
            if op == "/":
                return flat(l, "((%s)*%s)" % (curr, r))

    l, _,  r = collapsed["root"]

    expr = flat(l, str(r)) if isinstance(r, int) else flat(r, str(l))

    def evaluate(expr):

        evaluate.pos = 0

        def evaluate_expr():
            evaluate.pos += 1

            if expr[evaluate.pos].isdigit():
                l = evaluate_num()
            elif expr[evaluate.pos] == '(':
                l = evaluate_expr()
            else:
                raise Exception("invalid char at evaluate.pos %s: %s" % (evaluate.pos, expr[evaluate.pos]))

            if expr[evaluate.pos] == ')' and isinstance(l, int):
                evaluate.pos += 1
                return l

            op = expr[evaluate.pos]

            evaluate.pos += 1

            if expr[evaluate.pos].isdigit():
                r = evaluate_num()
            elif expr[evaluate.pos] == '(':
                r = evaluate_expr()
            else:
                raise Exception("invalid char at evaluate.pos %s: %s", evaluate.pos, expr[evaluate.pos])

            evaluate.pos += 1

            return eval("%s %s %s" % (l, op, r))

        def evaluate_num():
            s = ''
            while expr[evaluate.pos].isdigit():
                s += expr[evaluate.pos]
                evaluate.pos += 1
            return int(s)

        return evaluate_expr()

    return evaluate(expr)


def parse(input):
    parse_deps = lambda s: int(s) if s.isdigit() else tuple(s.split(' '))
    return dict((line.split(":")[0], parse_deps(line.split(":")[1].strip())) for line in input.splitlines())


def main():
    input = open("input", "r").read()
    print(solution(parse(input)))


main()
