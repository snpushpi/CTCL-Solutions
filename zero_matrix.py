def zero_matrix(matrix):
    zero_row = set()
    zero_col = set()
    l = len(matrix)
    for i in range(l):
        for j in range(l):
            if matrix[i][j]==0:
                zero_row.add(i)
                zero_col.add(j)
    for row in zero_row:
        for i in range(l):
            matrix[row][l]=0
    for col in zero_col:
        for i in range(l):
            matrix[i][col]=0
    return matrix