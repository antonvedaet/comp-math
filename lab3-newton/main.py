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


def transform_equations(funcs, x):
    return [func(x) for func in funcs]

def jacobian(funcs, x):
    h = 1e-5
    jac = []
    for i in range(len(x)):
        row = []
        for j in range(len(x)):
            df_dx = (funcs[i]([x[k] + (h if k == j else 0) for k in range(len(x))]) - funcs[i](x)) / h
            row.append(df_dx)
        jac.append(row)
    return jac

def multiply_matrix_vector(matrix, vector):
    return [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]

def inverse_matrix(matrix):
    n = len(matrix)
    identity_matrix = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for i in range(n):
        if matrix[i][i] == 0:
            continue

        pivot = matrix[i][i]
        for j in range(i, n):
            matrix[i][j] /= pivot
        for j in range(n):
            identity_matrix[i][j] /= pivot

        for k in range(i + 1, n):
            coefficient = matrix[k][i]
            for j in range(i, n):
                matrix[k][j] -= coefficient * matrix[i][j]
            for j in range(n):
                identity_matrix[k][j] -= coefficient * identity_matrix[i][j]

    for i in range(n - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            coefficient = matrix[k][i]
            for j in range(n):
                identity_matrix[k][j] -= coefficient * identity_matrix[i][j]

    return identity_matrix

def iterate(funcs, x):
    jac = jacobian(funcs, x)
    f_val = transform_equations(funcs, x)

    jac_inv = inverse_matrix(jac)

    delta = multiply_matrix_vector(jac_inv, f_val)

    x_new = [x[i] - delta[i] for i in range(len(x))]

    return x_new

def solve_by_fixed_point_iterations(system_id, number_of_unknowns, initial_approximations):
    funcs = get_functions(system_id)

    x = initial_approximations

    max_iter = 1000

    epsilon = 0.0001

    for _ in range(max_iter):
        x_new = iterate(funcs, x)
        sum_of_squares = sum((x_new[i] - x[i]) ** 2 for i in range(number_of_unknowns))
        if sum_of_squares ** 0.5 < epsilon:
            return x_new
        x = x_new
    raise ValueError(f"The method did not converge after {max_iter} iterations")


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