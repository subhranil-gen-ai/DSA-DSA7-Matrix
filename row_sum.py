def row_sum(matrix):
  for i in range(len(matrix)):
    total=sum(matrix[i])
    print(total)
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(row_sum(matrix))
