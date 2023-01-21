'''3. Write a python program to find mean and median of a set of elements.'''

# solution
list=[3,6,9,7,1,2,6,0,4,11]
list.sort() # sort
# print (list)
n=len(list)
mean=sum(list)/n
if n%2==0:
  median=(list[n//2]+list[(n//2)-1])/2
else:
  median=list[n//2]

print(f"The mean of the given data set is {mean} and the median of the given data set is {median}")