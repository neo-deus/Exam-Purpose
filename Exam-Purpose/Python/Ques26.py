'''26. Write programs to find the sum of the following series: x - x^2 /2! + x^3 /3! - x^4 /4! +
x^5 /5! - x^6 /6! (Input x)'''

# solution
x=int(input("Enter the value for x : "))

def fact(n):
  prod=1
  for i in range(n):
    prod=prod*(i+1)
  return prod
sum=0
for i in range(6):
  if i%2==0:
    sum+=pow(x,i+1)/fact(i+1)
  else:
    sum-=pow(x,i+1)/fact(i+1)
print(f"The sum of the given series is {sum}")