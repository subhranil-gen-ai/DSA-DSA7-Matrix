def sum_row_bound(matrix):
  n=len(matrix)
  for i in range(n):
    first_row=sum(matrix[0])
    last_row=sum(matrix[n-1])
    total1=first_row+last_row
  return total1

def sum_col_bound(matrix):
  n=len(matrix)
  first_col=0
  last_col=0
  for i in range(1,n-1):
    first_col+= matrix[i][0]
    last_col+= matrix[i][-1]
  total2=first_col+last_col
  return total2

def sum_boundary(matrix):
  return sum_row_bound(matrix)+sum_col_bound(matrix)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_row_bound(matrix))
print(sum_col_bound(matrix))
print(sum_boundary(matrix))
