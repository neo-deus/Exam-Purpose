'''61. Write a python program to create an 3X3 Matrix randomly and calculate sum of
the diagonal elements.'''

# solution
from numpy import random
a=random.randint(100,size=(3,3))
print("Random 3X3 Matrix : ")
print(a)
sum=0
for i in range(3):
  for j in range(3):
    if i == j:
      sum+=a[i][j]
print(f"Sum of diagonal elements is : {sum}")