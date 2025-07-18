def print_matrix_column_wise(matrix):
  rows=len(matrix)
  cols=len(matrix[0])
  for col in range(cols):
    for row in range(rows):
      print(matrix[row][col],end=" ")
    print()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(print_matrix_column_wise(matrix))
