'''27. Write a Python program using a function to check whether a given number is an ugly
number. In number system, ugly numbers are positive numbers whose only prime
factors are 2, 3 or 5. First 10 ugly numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12. By
convention, 1 is included.'''

# solution
def ugly(n):
  x=1
  while n!=1:
    if n%2==0:
      n=n//2
    elif n%3==0:
      n=n//3
    elif n%5==0:
      n=n//5
    else:
      x=0
      break
  return x
    
n=int(input("Enter the no : "))
ans=ugly(n)
if(ans==1):
  print("It is an ugly number")
else:
  print("It is not an ugly number")