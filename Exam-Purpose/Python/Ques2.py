'''2. Write a program to take a year as input and check If it is a leap year or not.'''

# solution
a=int(input("Enter a year: "))
if a%4==0:
  if a%100==0 and a%400!=0:
    print("It is not a leap year")
  else:
    print("It is a leap year")
else:
  print("It is not a leap year")
