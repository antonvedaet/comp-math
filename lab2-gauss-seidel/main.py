#!/bin/python3

import math
import os
import random
import re
import sys

class Result:
    isMethodApplicable = True
    errorMessage = ""

    def applicable(n, matrix, epsilon):
        for i in range(n):
            sum_of_abs = sum(abs(matrix[i][j]) for j in range(n) if i != j)
            if abs(matrix[i][i]) <= sum_of_abs:
                Result.isMethodApplicable = False
                Result.errorMessage = "The system has no diagonal dominance for this method. Method of the Gauss-Seidel is not applicable."
                return False
        return True
    
    
    def solveByGaussSeidel(n, matrix, epsilon):
        if not Result.applicable(n, matrix, epsilon):
            return []
        
        solution = [0.0] * n

        while True:
            new_solution = [0.0] * n
            for i in range(n):
                sum_of_elements = sum(matrix[i][j] * solution[j] for j in range(n) if i != j)
                new_solution[i] = (matrix[i][n] - sum_of_elements) / matrix[i][i]
            if all(abs(new_solution[i] - solution[i]) < epsilon for i in range(n)):
                return new_solution

            solution = new_solution
            
            
if __name__ == '__main__':
    n = int(input().strip())

    matrix_rows = n
    matrix_columns = n+1

    matrix = []

    for _ in range(matrix_rows):
        matrix.append(list(map(float, input().rstrip().split())))

    epsilon = float(input().strip())

    result = Result.solveByGaussSeidel(n, matrix, epsilon)
    if Result.isMethodApplicable:
        print('\n'.join(map(str, result)))
    else:
        print(f"{Result.errorMessage}")
