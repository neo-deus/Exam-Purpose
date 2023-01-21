'''22. Write Python programs to sum the given sequences up to n terms: 2/9 - 5/13 + 8/17......'''

# solution
n=int(input("Enter a number : "))
sum=0
for i in range(n):
  if (i+1)%2 != 0:
    sum+=(2+(i*3))/(9+4*i)
  else:
    sum-=(2+(i*3))/(9+4*i)
print(f"The sum of the given series upto {n} terms is {sum}")