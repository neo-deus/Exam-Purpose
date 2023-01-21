'''28. Write a Python program to sum the sequence: 1 + 1/1! + 1/2! + 1/3! + ..... + 1/n!
(Input n through keyboard)'''

# solution
n=int(input("Enter a number n : "))
sum=1
def fact(n):
  prod=1
  for i in range(n):
    prod=prod*(i+1)
  return prod
for i in range(n):
  sum+=1/fact(i+1)
print(f"The sum of the given series is {sum}")