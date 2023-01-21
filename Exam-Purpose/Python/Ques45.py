'''45. Write a Python script to print all Prime numbers between 1 to n.'''

# solution
def prime_factor(v):
  flag=False
  for i in range(2,v):
    if v%i==0:
      flag=True
      break
  if flag==False:
    print(v,end=' ')

n=int(input("Enter the range : "))
print("The prime numbers are : ")
for i in range(2,n+1):
  prime_factor(i)