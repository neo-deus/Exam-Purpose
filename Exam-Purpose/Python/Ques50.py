'''50. Write a Python script for following…
An electric distribution companies arranges its domestic consumer as follows:
      Consumption in Units    Rate of charge
      0 – 200                 Rs. 0.50 per unit
      201 – 400               Rs. 100 plus Rs. 0.65 per unit excess to 200
      400 – 600               Rs. 250 plus Rs. 0.80 per unit excess to 400
      Above 600               Rs. 425 plus Rs. 1.25 per unit excess to 600
Print the amount to be paid by consumer.'''

# solution
n=int(input("Enter the amount of units consumed : "))
if n>=0:
  if n<=200:
    print(f"The electricity bill is Rs.{n*0.5}")
  elif n<=400:
    print(f"The electricity bill is Rs.{100+(n-200)*0.65}")
  elif n<=600:
    print(f"The electricity bill is Rs.{250+(n-400)*0.8}")
  else:
    print(f"The electricity bill is Rs.{425+(n-600)*1.25}")
else:
  print("Invalid unit")