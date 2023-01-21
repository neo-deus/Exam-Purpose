'''19. Write a Python Program to print the Prime Factors of an Integer.'''

# solution
def prime_factor(v):
  flag=False
  for i in range(2,v):
    if v%i==0:
      flag=True
      break
  if flag==False:
    print(v,end=' ')

n=int(input("Enter the number : "))
print("The prime factors are : ")
for i in range(2,n+1):
  if n%i==0:
    prime_factor(i)
