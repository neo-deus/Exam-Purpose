'''10. Write a Python program to print every integer between 1 and n divisible by m. Also
report whether the number that is divisible by m is even or odd.'''

# solution
n=int(input("Enter the limit : "))
m=int(input("Enter the number : "))
for i in range(1,n+1):
  if i%m == 0:
    if i%2==0:
      print(f"{i} is even")
    else:
      print(f"{i} is odd")