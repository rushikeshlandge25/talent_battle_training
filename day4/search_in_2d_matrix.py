target=3
matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]==target:
            print("Found At index",i,j)