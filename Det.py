def matrix_minor(matrix,a,b):
    return [a[:b] + a[b + 1:] for a in (matrix[:a] + matrix[a + 1:])]

def determinant(matrix):
    j = len(matrix)
    if j == 1:
        return matrix[0][0]

    det = 0
    for i in range(j):
        sign = (-1) ** i
        cofactor = determinant(matrix_minor(matrix,0,i))
        det += sign * matrix[0][i] * cofactor

    return det

j = int(input("Give the size of  matrix:"))
if j <= 0:
    print("Given a Wrong Values for the size!")
matrix = []
for r in range(j):
    a = list(map(int,input(f"Give the elements of row {r} :").split()))
    if len(a) != j:
        print("No.of rows not equal to given size!!")
    matrix.append(a)
if len(matrix) != j:
    print("Given length is not matching")

det = determinant(matrix)
print("Determinant =",det)

