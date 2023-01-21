'''42. Write a Python script to find all roots of a quadratic equation for all possible combination of a, b and c.'''

# solution
import math
print("Quadratic equation ax^2+bx+c=0")
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
D=b**2-4*a*c
print(D)
if D>0:
  x1=(-b+math.sqrt(D))/(2*a)
  x2=(-b-math.sqrt(D))/(2*a)
  print(f"The roots of the equation are real and different and they are {x1} and {x2}")
elif D==0:
  x=-b/(2*a)
  print(f"The roots of the equation are real and same and they are {x} and {x}")
else:
  x1=-b/(2*a)
  i=(math.sqrt(-D))/(2*a)
  print(f"The roots of the equation are complex and they are {x1}+{i}i and {x1}-{i}i")