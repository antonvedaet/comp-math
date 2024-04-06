#!/bin/python3

import math
import os
import random
import re
import sys


k = 0.4
a = 0.9

def first_function(args: []) -> float:
    return math.sin(args[0])


def second_function(args: []) -> float:
    return (args[0] * args[1]) / 2


def third_function(args: []) -> float:
    return math.tan(args[0]*args[1] + k) - pow(args[0], 2)


def fourth_function(args: []) -> float:
    return a * pow(args[0], 2) + 2 * pow(args[1], 2) - 1


def fifth_function(args: []) -> float:
    return pow(args[0], 2) + pow(args[1], 2) + pow(args[2], 2) - 1


def six_function(args: []) -> float:
    return 2 * pow(args[0], 2) + pow(args[1], 2) - 4 * args[2]


def seven_function(args: []) -> float:
    return 3 * pow(args[0], 2) - 4 * args[1] + pow(args[2], 2)


def default_function(args: []) -> float:
    return 0.0


# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        k = 0.4
        a = 0.9
        return [third_function, fourth_function]
    elif n == 3:
        k = 0
        a = 0.5
        return [third_function, fourth_function]
    elif n == 4:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]

def transform(fs, xs):
    return [fs[i](xs[i]) for i in range(len(fs))]

def jacobian(funcs, vars_values):
    n = len(funcs)
    m = len(vars_values)
    h = 1e-8

    J = []
    for i in range(n):
        row = []
        for j in range(m):
            dx = [0] * m
            dx[j] = h
            f_plus = funcs[i](*[var + dvar for var, dvar in zip(vars_values, dx)])
            f_minus = funcs[i](*[var - dvar for var, dvar in zip(vars_values, dx)])
            row.append((f_plus - f_minus) / (2 * h))
        J.append(row)

    return J
        

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    funcs = get_functions(system_id)
    return jacobian(funcs, initial_approximations)


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)

    print('\n'.join(map(str, result)))
    print('\n')