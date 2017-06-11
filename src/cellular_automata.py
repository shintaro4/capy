# -*- coding: utf-8 -*-

import argparse


# constants
RULE_SEQUENCE_SIZE = 8
INITIAL_CELLS = [True]


def init_rule(number):
    """
    returns a boolean list expression of the rule number.
    """
    if number < 0 or number > 2 ** RULE_SEQUENCE_SIZE - 1:
        raise ValueError()

    return list(map(lambda x: True if number & x else False,
                    [1 << i for i in range(RULE_SEQUENCE_SIZE)]))


def next(rule, cells):
    """
    returns the next generations.
    """
    def f(i):
        l = 4 if 0 <= i - 1 < len(cells) and cells[(i - 1) % len(cells)] else 0
        c = 2 if 0 <= i < len(cells) and cells[i] else 0
        r = 1 if 0 <= i + 1 < len(cells) and cells[(i + 1) % len(cells)] else 0
        return rule[l + c + r]

    return list(map(lambda x: f(x), range(-1, len(cells) + 1)))


def print_cells(cells, n):
    """
    prints cells nicely.
    """
    padding = [' '] * n
    s = ''.join(padding + ['o' if c else ' ' for c in cells])
    print(s)


def main(rule_number, n):
    """
    main function.
    """
    if n < 0:
        raise ValueError()

    rule = init_rule(rule_number)
    cells = INITIAL_CELLS
    for i in range(n):
        print_cells(cells, n - i)
        cells = next(rule, cells)


def init_arg_parser():
    """
    initialize command line arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--rule', help="a rule number",
                        type=int, default=110)
    parser.add_argument('--n', help="the number of the generations",
                        type=int, default=16)
    return parser


if __name__ == "__main__":
    parser = init_arg_parser()
    args = parser.parse_args()
    main(args.rule, args.n)
