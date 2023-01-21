'''48. Write a Python script to print Fibonacci series up to n terms.'''

# solution
n=int(input("Enter the number of elements : "))
def fib(n):
  a=0
  b=1
  print(a,b,end=" ")
  for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print(f"The Fibonacci numbers upto {n} terms are : ")
fib(n)