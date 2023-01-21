'''60. Input two 3X3 Matrixes. Now perform
      a. the addition of two 3X3 Matrixes.
      b. perform the elements-wise multiplication of two 3X3 Matrixes.
      c. perform the Matrix Multiplication of two 3X3 Matrixes.'''

# solution
l1=[[0,0,0],[0,0,0],[0,0,0]]
l2=[[0,0,0],[0,0,0],[0,0,0]]
l3=[[0,0,0],[0,0,0],[0,0,0]]
def display(l):
  for i in range(3):
    for j in range(3):
      print(l[i][j],end=" ")
    print()
print("Enter the elements of first matrix : ")
for i in range(3):
  for j in range(3):
    l1[i][j]=int(input())
print("Enter the elements of second matrix : ")
for i in range(3):
  for j in range(3):
    l2[i][j]=int(input())
for i in range(3):   # matrix addition
  for j in range(3):
    l3[i][j]=l1[i][j]+l2[i][j]
print("Matrix 1 : ")
display(l1)
print("Matrix 2 : ")
display(l2)
print("Sum of matrix 1 and 2 : ")
display(l3)
for i in range(3):   # element wise multiplication
  for j in range(3):
    l3[i][j]=l1[i][j]*l2[i][j]
print("Element wise multiplication of matrix 1 and 2 :")
display(l3)
for i in range(3):   # matrix multiplication
  for j in range(3):
    sum=0
    for k in range(3):
      sum+=l1[i][k]*l2[k][j]
      l3[i][j]=sum
print("Matrix multiplication of Matrix 1 and 2 : ")
display(l3)