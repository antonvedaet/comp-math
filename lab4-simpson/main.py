#!/bin/python3

import math
import os
import random
import re
import sys


class Result:
    error_message = ""
    has_discontinuity = False
    eps = 0
    def first_function(x: float):
        try:
            return 1 / x
        except ZeroDivisionError:
            return None

    def second_function(x: float):
        if x == 0:
            return (math.sin(Result.eps)/Result.eps + math.sin(-Result.eps)/-Result.eps)/2 
        return math.sin(x)/x


    def third_function(x: float):
        return x*x+2


    def fourth_function(x: float):
        return 2*x+2


    def five_function(x: float):
        try: 
            return math.log(x)
        except ValueError:
            return None

    # How to use this function:
    # func = Result.get_function(4)
    # func(0.01)
    def get_function(n: int):
        if n == 1:
            return Result.first_function
        elif n == 2:
            return Result.second_function
        elif n == 3:
            return Result.third_function
        elif n == 4:
            return Result.fourth_function
        elif n == 5:
            return Result.five_function
        else:
            raise NotImplementedError(f"Function {n} not defined.")

    #
    # Complete the 'calculate_integral' function below.
    #
    # The function is expected to return a DOUBLE.
    # The function accepts following parameters:
    #  1. DOUBLE a
    #  2. DOUBLE b
    #  3. INTEGER f
    #  4. DOUBLE epsilon
    #
    def simpson(a, b, f, n):
        h = (b - a) / n
        fa = f(a)
        fb = f(b)
        if fa == None or fb == None:
            return None
        s = fa + fb
        for i in range(1, n, 2):
            f_i = f(a + i * h)
            if f_i == None:
                return None
            s += 4 * f_i
        for i in range(2, n - 1, 2):
            f_i = f(a + i * h)
            if f_i == None:
                return None
            s += 2 * f_i
        return s * h / 3

    def calculate_integral(a, b, f, epsilon):
        if a > b:
            Result.has_discontinuity = True
            Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
            return None
        Result.eps = epsilon
        f = Result.get_function(f)
        ans = 0
        n = 2
        p_ans = Result.simpson(a, b, f, n)
        if p_ans == None:
            Result.has_discontinuity = True
            Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
            return None
        while True:
            n *= 2
            ans = Result.simpson(a,b,f,n)
            if ans == None:
                Result.has_discontinuity = True
                Result.error_message = "Integrated function has discontinuity or does not defined in current interval"
                return None
            if abs(ans - p_ans) < epsilon:
                return ans
            p_ans = ans
        return ans


if __name__ == '__main__':

    a = float(input().strip())

    b = float(input().strip())

    f = int(input().strip())

    epsilon = float(input().strip())

    result = Result.calculate_integral(a, b, f, epsilon)
    if not Result.has_discontinuity:
        print(str(result) + '\n')
    else:
        print(Result.error_message + '\n')
