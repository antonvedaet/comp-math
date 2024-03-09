class Result:
    isMethodApplicable = True
    errorMessage = ""

    def solveByGaussSeidel(n, matrix, epsilon):
        #TODO implement method
        
        return []
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
