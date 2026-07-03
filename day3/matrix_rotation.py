matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

output=[[7,4,1],
        [8,5,2],
        [9,6,3]]
row=len(matrix)
col=len(matrix[0])

ans=[[0]*col for i in range(row)]
n=len(matrix)
print("Original Matrix:")
for i in range(n):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()
n=len(matrix)
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        ans[j][n-1-i]=matrix[i][j]

print("Rotated Matrix:")

for i in range(n):
    for j in range(len(ans[i])):
        print(ans[i][j],end=" ")
    print()
