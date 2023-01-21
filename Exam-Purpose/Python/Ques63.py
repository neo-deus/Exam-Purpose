'''63. Read two matrix and add them. Store the matrices and result in a file.'''

# solution
def read(file):
  with open(file) as f:
    m=[]
    for line in f:         #iterates over each row
      m.append([int(x) for x in line.split()])  
    return m
matrix1 = read("matrix1.txt")#reads matrix1.txt
matrix2 = read("matrix2.txt")
print(matrix1)
result = []
for i in range(len(matrix1)):   #iterates over no. of rows(by default)
  row = []
  for j in range(len(matrix1[0])):   #iterates over no. of columns
    row.append(matrix1[i][j] + matrix2[i][j])
  result.append(row)
# store matrices and result in a file
with open("matrices_result.txt", "w") as f:
  f.write("Matrix 1:\n")
  for row in matrix1:         #iterates over each item in matrix1 which are individual rows
    f.write(" ".join(str(x) for x in row) + "\n")#joins each element with spaces and converts to a string, then writes 
  f.write("Matrix 2:\n")
  for row in matrix2:
    f.write(" ".join(str(x) for x in row) + "\n")
  f.write("Result:\n")
  for row in result:
    f.write(" ".join(str(x) for x in row) + "\n")