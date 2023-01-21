'''43. Write a Python script to find HCF (GCD) and LCM of two numbers.'''

# solution
m=int(input("Enter first number : "))
n=int(input("Enter second number : "))
def gcd(m,n):
  i=1
  while i<=m and i<=n:
    if m%i==0 and n%i==0:
      t=i
      i+=1
    else:
      i+=1
  return t
def gcd1(a, b):
  if (a == 0):
    return b
  if (b == 0):
    return a
  if (a == b):
    return a
  if (a > b):
    return gcd(a-b, b)
  return gcd(a, b-a)
print(f"The HCF(GCD) of the given numbers is {gcd1(m,n)}\nAnd the LCM of the given numbers is {int(m*n/gcd1(m,n))}")