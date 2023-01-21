'''7. Write a program to input 3 sides of a triangle and print whether it is an equilateral, scalene or isosceles triangle.'''

# solution
a=int(input("Enter side 1 of triangle : "))
b=int(input("Enter side 2 of triangle : "))
c=int(input("Enter side 3 of triangle : "))
if a>0 and b>0 and c>0:
  if a==b and c==b:
    print("It is an equilateral triangle")
  elif a==c or b==c or c==a:
    print("It is an isosceles triangle")
  else:
    print("It is a scalene triangle")
else:
  print("Invalid triangle")