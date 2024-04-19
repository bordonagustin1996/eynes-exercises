def transpose(matrix):
    row = len(matrix)
    column = len(matrix[0])
    return [[matrix[j][i] for j in range(row)] for i in range(column)]