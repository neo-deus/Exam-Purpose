'''11. Write a python program to find out the palindromic prime numbers between a range.'''

# solution
n=int(input("Enter the lower limit : "))
m=int(input("Enter the upper limit : "))

def prime(z):
  flag=False
  for i in range(2,z):
    if z%i==0:
      flag=True
      break
  if flag==False:
    print (f"{z} is a palindromic prime number")

def palindrome(v):
  dup=v
  s=0
  while dup>0:
    s=s*10+(dup%10)
    dup=dup//10
  if s==v:
    prime(s)

for i in range(n,m+1):
  palindrome(i)
