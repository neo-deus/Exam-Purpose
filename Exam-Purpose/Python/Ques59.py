'''59.Write a program to reverse a list without using another list or in-built function.'''

# solution
l=[1,2,3,4,5,6,7,8,9,0,4]
print("Initial list : ",l)
j=len(l)-1
for i in range(len(l)//2):
  l[i],l[j] = l[j],l[i]
  j-=1
print("Reversed list : ",l)