
# operators: + - * / ** (exponentiation)

def parse_number(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return None


def func_product(args):
    result = 1
    for arg in args:
        result *= arg

    return result


def func_quotient(args):
    first, *rest = args
    result = first
    for arg in rest:
        result /= arg

    return result


def func_difference(args):
    first, *rest = args
    result = first
    for arg in rest:
        result -= arg

    return result


def func_exponent(args):
    first, *rest = args
    result = first
    for arg in rest:
        result **= arg

    return result


def parse_func(name):
    return {
        '+': sum,
        '-': func_difference,
        '*': func_product,
        '/': func_quotient,
        '**': func_exponent
    }[name]


def evaluate(tree):
    if type(tree) is not list:
        return tree

    func, *args = tree
    evaluated_args = [evaluate(arg) for arg in args]
    return func(evaluated_args)


def tokenize(sexpr):
    # -34.5
    # (+ 1 (** 2.3 -3))
    # (+ 1(/ 2 3))
    # ... just put a space before and after each paren and be done with it
    return sexpr.replace('(', ' ( ').replace(')', ' ) ').split()


def parse(tokens):
    result = []
    ancestors = [] # stack

    def current_list():
        if ancestors:
            return ancestors[-1]
        else:
            return result

    for token in tokens:
        if token == '(':
            ancestors.append([])
        elif token == ')':
            done = ancestors.pop()
            current_list().append(done)
        else:
            num = parse_number(token)
            if num is not None:
                current_list().append(num)
            else:
                current_list().append(parse_func(token))

    if len(ancestors) != 0:
        raise Exception('unbalanced parentheses')

    return result[0]


def repl():
    while True:
        try:
            line = input('sexpr> ')
        except EOFError:
            print()
            break

        try:
            print(evaluate(parse(tokenize(line))))
        except Exception as error:
            print(error)


if __name__ == '__main__':
    repl()
