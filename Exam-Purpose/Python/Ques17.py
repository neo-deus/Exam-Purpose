'''17. Write a Python function that takes a list and returns a new list with unique elements
of the first list.
Sample List : [1,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]'''

l1=[1,2,3,3,3,3,4,5]
l2=[]
for i in l1:
  if i not in l2:
    l2.append(i)
print("Sample List : ",l1)
print("Unique List : ",l2)