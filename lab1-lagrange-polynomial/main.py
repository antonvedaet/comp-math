import math
import os
import random
import re
import sys


def interpolate_by_lagrange(x_axis, y_axis, x):
    result = 0
    for i in range(len(x_axis)):

        p = y_axis[i]

        for j in range(len(x_axis)):

            if i != j:
                p *= ((x - x_axis[j]) / (x_axis[i] - x_axis[j]))
                
        result += p

    return result

def run_tests():
    assert interpolate_by_lagrange([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5) == 15.625

    assert interpolate_by_lagrange([1.5, 2.5, 3.5], [2.25, 6.25, 12.25], 2) == 4

    assert round(interpolate_by_lagrange([-1, -0.5, 0, 0.5], [1, 0.25, 0, 0.25], -0.2), 2) == 0.04

    assert interpolate_by_lagrange([1, 2, 3, 4], [1, 4, 9, 16], 2.5) == 6.25
    
    assert interpolate_by_lagrange([-1, 0, 1, 2], [1, 0, 1, 8], 0.5) == 0

    print("all tests passed")


if __name__ == "__main__":

    run_tests()















    # xs = [float(i) for i in input().split()]
    # ys = [float(i) for i in input().split()]
    # x = float(input())

    # print(interpolate_by_lagrange(xs,ys,x))
    