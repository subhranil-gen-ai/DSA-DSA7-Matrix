def transpose_matrix(matrix):
  rows=len(matrix)
  cols=len(matrix[0])
  transposed=[]
  for col in range(cols):
    new_matrix=[]
    for row in range(rows):
      new_matrix.append(matrix[row][col])
    transposed.append(new_matrix)
  return transposed
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(transpose_matrix(matrix))
