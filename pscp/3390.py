"""Array 2D"""
matrix = []
for _ in range(5):
    x = list(map(int, input().split()))
    matrix.append(x)

row = -1
column = -1

for i in range(5):
    row_sum = sum(matrix[i])
    if row_sum % 2:
        row = i

for j in range(5):
    col_sum = 0
    for k in range(5):
        col_sum += matrix[k][j]

    if col_sum % 2:
        column = j

print(row, column)
