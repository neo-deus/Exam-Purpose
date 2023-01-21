'''40. Write a program to convert centigrade to Fahrenheit and reverse also.'''

# solution
n=int(input("Enter 1 for Celcius to Fahrenheit and 2 for Fahrenheit to Celsius : "))
if n==1:
  c=float(input("Enter the temperature in degree Celcius : "))
  f=c*(9/5)+32
  print(f"The corresponding temperature in Fahrenheit is {f} degrees")
elif n==2:
  f=float(input("Enter the temperature in degree Fahrenheit : "))
  c=(f-32)*5/9
  print(f"The corresponding temperature in Celcius is {c} degrees")
else:
  print("Invalid option")
