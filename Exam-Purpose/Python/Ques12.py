'''12.Write a python program to find the Twins primes between a range( Twin primes are
      pairs of prime numbers that have just one number between them: 5 and 7, 11 and
      13,and 29 and 31).'''

# solution
def checkprime(num):
  count=0
  for i in range(2,num):
    if(num%i==0):
      count+=1
  if(count>0):
    return 0
  else:
    return 1
n=int(input("Enter the range to find twin primes : "))
print("The twin primes are : ")
for i in range(2,n+1):
  n1=i
  n2=i+2
  if(checkprime(n1) and checkprime(n2)):
    print(n1,"and",n2)