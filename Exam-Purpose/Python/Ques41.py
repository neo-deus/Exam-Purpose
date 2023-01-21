'''41. Write a Python script to enter length and breadth of a rectangle and radius of a circle.
Find perimeter and area of rectangle and circumference and area of circle.'''

# solution
n=int(input("Enter 1 for area of rectangle and 2 for radius of circle : "))
if n==1:
  l=float(input("Enter length of rectangle : "))
  b=float(input("Enter breadth of rectangle : "))
  area=l*b
  peri=2*(l+b)
  print(f"Area of rectangle is : {area} and the perimeter of rectangle is : {peri}")
elif n==2:
  r=float(input("Enter radius of circle : "))
  area=3.14*r*r
  cir=2*3.14*r
  print(f"Area of circle is : {area} and the circumference of circle is : {cir}")
else:
  print("Invalid option")
