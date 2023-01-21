'''46. Write a Python script to check whether a number is Armstrong number or not.'''

# solution
n=int(input("Enter a number : "))
d=n
c=len(str(n))
s=0
while d>0:
  s+=pow(d%10,c)
  d=d//10
if s==n:
  print(f"{n} is a Armstrong number")
else:
  print(f"{n} is not a Armstrong number")