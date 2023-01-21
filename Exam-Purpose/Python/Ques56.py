'''56.Write a program to display the maximum and minimum values from the
specified range of indexes of list.'''

# solution
l=[3,8,0,8,6,4,444,2,239,4,834,127,111,769,13,444,987,6,6,4,5,3,555,323]
l1=len(l)
print(f"Length of list is {l1}")
m=int(input("Enter the lower limit : "))
n=int(input("Enter the upper limit : "))
if n<0 or n>l1 or m<0 or m>l1:
  print("Invalid parameters")
else:
  max=l[m]
  min=l[m]
  for i in range(m+1,n+1):
    if max<l[i]:
      max=l[i]
    elif min>l[i]:
      min=l[i]
  print(f"Maximum value in given range is {max} and minimum value is {min}")
