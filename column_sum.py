def column_sum(matrix):
  rows=len(matrix)
  colums=len(matrix[0])
  for col in range(colums):
    total=0
    for row in range(rows):
      total+=matrix[row][col]
    print(total)
   
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(column_sum(matrix))
