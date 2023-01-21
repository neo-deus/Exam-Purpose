'''49. Write a Python script to find value of following series: y=1+1/2+1/3+...+1/n where is user input.'''

# solution
n=int(input("Enter a number : "))
s=0
for i in range(n):
  s+=1/(i+1)
print(f"The sum of the series 1+1/2+1/3+...+1/n upto {n} terms is {s}")