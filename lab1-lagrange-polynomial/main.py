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

xs = [float(i) for i in input().split()]
ys = [float(i) for i in input().split()]
x = float(input())

print(interpolate_by_lagrange(xs,ys,x))