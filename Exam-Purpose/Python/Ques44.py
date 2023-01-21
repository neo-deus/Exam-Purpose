'''44. Write a Python script to check whether a number is Prime number or not.'''

# solution
def prime_factor(v):
  flag=False
  if v==1:
    flag=True
  for i in range(2,v):
    if v%i==0:
      flag=True
      break
  if flag==False:
    print(f"{v} is a prime number")
  else:
    print(f"{v} is not a prime number")

n=int(input("Enter the number : "))
prime_factor(n)