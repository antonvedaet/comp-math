#!/bin/python3

import math
import os
import random
import re
import sys

class Result:
    isMethodApplicable = True
    errorMessage = ""

    def is_applicable(n, matrix, epsilon):
        for i in range(n):
            sum_of_abs = sum(abs(matrix[i][j]) for j in range(n) if i != j)
            if abs(matrix[i][i]) <= sum_of_abs:
                Result.isMethodApplicable = False
                Result.errorMessage = "The system has no diagonal dominance for this method. Method of the Gauss-Seidel is not applicable."
                return False
        return True
    
    
    def solveByGaussSeidel(n, matrix, epsilon):
        if not Result.is_applicable(n, matrix, epsilon):
            return []
        
        tmp = [0.0] * n

        while True:
            result = [0.0] * n
            for i in range(n): 
                result[i] = (matrix[i][n] - sum(matrix[i][j] * tmp[j] for j in range(n) if i != j)) / matrix[i][i]
            if all(abs(result[i] - tmp[i]) < epsilon for i in range(n)):
                return result

            tmp = result
            
            

def test_is_applicable_and_solveByGaussSeidel():
    
    matrix = [[10, 1, 2, 13], [3, 8, 4, 27], [5, 6, 9, 38]]
    n = 3
    epsilon = 0.01
    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    assert Result.isMethodApplicable == False
    assert abs(result[0] - 1) < epsilon
    assert abs(result[1] - 2) < epsilon
    assert abs(result[2] - 3) < epsilon

    matrix = [[-10, -1, -2, -13], [-3, -8, -4, -27], [-5, -6, -9, -38]]
    n = 3
    epsilon = 0.01
    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    assert Result.isMethodApplicable == True
    assert abs(result[0] - 1) < epsilon
    assert abs(result[1] - 2) < epsilon
    assert abs(result[2] - 3) < epsilon

    matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]
    n = 3
    epsilon = 0.01
    Result.solveByGaussSeidel(n, matrix, epsilon)
    assert Result.isMethodApplicable == False
    assert Result.errorMessage == "The system has no diagonal dominance for this method. Method of the Gauss-Seidel is not applicable."

    matrix = [[0, 2, 3, 4], [4, 0, 6, 7], [7, 8, 0, 10]]
    n = 3
    epsilon = 0.01
    Result.solveByGaussSeidel(n, matrix, epsilon)
    assert Result.isMethodApplicable == False
    assert Result.errorMessage == "The system has no diagonal dominance for this method. Method of the Gauss-Seidel is not applicable."

    matrix = [[1e6, 1e5, 1e4, 1e6 + 1e5 + 1e4], [1e5, 1e6, 1e5, 1e6 + 1e5 + 1e5], [1e4, 1e5, 1e6, 1e6 + 1e5 + 1e4]]
    n = 3
    epsilon = 0.01
    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    assert Result.isMethodApplicable == True
    assert abs(result[0] - 1) < epsilon
    assert abs(result[1] - 1) < epsilon
    assert abs(result[2] - 1) < epsilon
            
if __name__ == '__main__':
    # n = int(input().strip())

    # matrix_rows = n
    # matrix_columns = n+1

    # matrix = []

    # for _ in range(matrix_rows):
    #     matrix.append(list(map(float, input().rstrip().split())))

    # epsilon = float(input().strip())

    # result = Result.solveByGaussSeidel(n, matrix, epsilon)
    # if Result.isMethodApplicable:
    #     print('\n'.join(map(str, result)))
    # else:
    #     print(f"{Result.errorMessage}")
    print(test_is_applicable_and_solveByGaussSeidel())
