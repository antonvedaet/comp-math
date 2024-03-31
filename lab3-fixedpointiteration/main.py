#!/bin/python3

import math
import os
import random
import re
import sys

from decimal import Decimal, getcontext


def first_function(args: []):
    return math.sin(args[0])


def second_function(args: []):
    return (args[0] * args[1]) / 2


def third_function(args: []):
    return pow(args[0], 2) * pow(args[1], 2) - 3 * pow(args[0], 3) - 6 * pow(args[1], 3) + 8


def fourth_function(args: []):
    return pow(args[0], 4) - 9 * args[1] + 2


def fifth_function(args: []):
    return args[0] + pow(args[0], 2) - 2 * args[1] * args[2] - 0.1


def six_function(args: []):
    return args[1] + pow(args[1], 2) + 3 * args[0] * args[2] + 0.2


def seven_function(args: []):
    return args[2] + pow(args[2], 2) + 2 * args[0] * args[1] - 0.3


def default_function(args: []):
    return 0.0

# How to use this function:
# funcs = Result.get_functions(4)
# funcs[0](0.01)
def get_functions(n: int):
    if n == 1:
        return [first_function, second_function]
    elif n == 2:
        return [third_function, fourth_function]
    elif n == 3:
        return [fifth_function, six_function, seven_function]
    else:
        return [default_function]


#
# Complete the 'solve_by_fixed_point_iterations' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts following parameters:
#  1. INTEGER system_id
#  2. INTEGER number_of_unknowns
#  3. DOUBLE_ARRAY initial_approximations
#


# def check(x, xn, eps):
#     for i in range(len(x)):
#         if(abs(x[i] - xn[i]) > eps):
#             return False
#     return True

# def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
#     system = get_functions(system_id)
#     approxs = initial_approximations
#     eps = 0.00001

#     for _ in range(10000):
#         approxs_new = [system[i](approxs) for i in range(number_of_unknowns)] 
#         if check(approxs, approxs_new, eps):
#             return approxs_new
#         approxs = approxs_new
#     raise RuntimeError("Did not converge after 10000 iterations")
def check(x, xn, eps):
    for i in range(len(x)):
        if(abs(x[i] - xn[i]) > eps):
            return False
    return True

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    system = get_functions(system_id)
    approxs = initial_approximations
    eps = 0.00001

    for _ in range(10000):
        approxs_new = [system[i](approxs) for i in range(number_of_unknowns)] 
        if check(approxs, approxs_new, eps):
            return approxs_new
        approxs = approxs_new
    raise RuntimeError("Did not converge after 10000 iterations")


if __name__ == '__main__':
    system_id = int(input().strip())

    number_of_unknowns = int(input().strip())

    initial_approximations = []

    for _ in range(number_of_unknowns):
        initial_approximations_item = float(input().strip())
        initial_approximations.append(initial_approximations_item)

    result = solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations)
    print('\n'.join(map(str, result)))

def test():
    init_g = [0,0]
    n=2
    sys = 1
    if solve_by_fixed_point_iterations(sys,n, init_g) == [0.0,0.0]:
        print("test passed")
    else:
        print("test failed")
    init_g = [1000,1000]
    n=2
    sys = 1
    if solve_by_fixed_point_iterations(sys,n, init_g) == [0.0,0.0]:
        print("test passed")
    else:
        print("test failed")
    init_g = [-2,2]
    n=2
    sys = 2
    if solve_by_fixed_point_iterations(sys,n, init_g) == [-2.0,2.0]:
        print("test passed")
    else:
        print("test failed")
    init_g = [11124,434]
    n=2
    sys = 1
    if solve_by_fixed_point_iterations(sys,n, init_g) == [-2.0,2.0]:
        print("test passed")
    else:
        print("test failed")
    init_g = [0,0,0]
    n=3
    sys = 3
    if solve_by_fixed_point_iterations(sys,n, init_g) == [0.01793,-0.24965,0.23555]:
        print("test passed")
    else:
        print("test failed")