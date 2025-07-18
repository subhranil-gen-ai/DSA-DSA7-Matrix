def secondary_diagonal(matrix):
  n=len(matrix)
  count=0
  for i in range(n):
    count+=matrix[i][n-1-i]
  return count
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(secondary_diagonal(matrix))
