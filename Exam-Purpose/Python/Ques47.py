'''47. Write a Python script to check whether a number is Perfect number or not.'''

# solution
n=int(input("Enter a number : "))
s=0
for i in range(1,n):
  if n%i==0:
    s+=i
if s==n:
  print(f"{n} is a Perfect number")
else:
  print(f"{n} is not a Perfect number")
