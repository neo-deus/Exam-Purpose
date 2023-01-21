'''29. write a program to input a list of numbers and test if a number is equal to the sum of
the cubes of its digits. Print that new list and find the smallest and greatest element of
that list.'''

# solution
n=int(input("Enter the number of elements : "))
l=[]
z=[]
def check(n):
  d=n
  sum=0
  while d>0:
    sum+=pow(d%10,3)
    d=d//10
  if sum==n:
    z.append(sum)

for i in range(n):
  m=int(input())
  l.append(m)
for i in l:
  check(i)
print(z)
z.sort()
print(f"The smallest element in the list is {z[0]} and the largest element in the list is {z[len(z)-1]}")