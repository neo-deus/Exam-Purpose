'''57.Write a program to move all duplicate values in a list to the end of the list.'''

# solution
l1=[2,3,0,5,5,5,9,8,7,7,1]
l2=[]
l3=[]
dict={}
for i in l1:
  if i in dict:
    dict[i]+=1
  else:
    dict[i]=1
for i in dict:
  if dict[i] ==1:
    l2.append(i)
  else:
    c=dict[i]
    for j in range(c):
      l3.append(i)
for i in l3:
  l2.append(i)
print("Initial list : ",l1)
print("Final list : ",l2)