'''54.Write a program that takes any two lists L and M of the same size and adds their
elements together to form a new list N whose elements are sums of the
corresponding elements in L and M. For instance, if L = [3, 1, 4] and M = [1, 5, 9],
then N should equal [4,6,13].'''

# solution
n=int(input("Enter the size of lists : "))
L=[]
M=[]
N=[]
print("Enter the elements of first list : ")
for i in range(n):
  L.append(int(input()))
print("Enter the elements of second list : ")
for i in range(n):
  M.append(int(input()))
for i in range(n):
  N.append(L[i]+M[i])
print("L=",L)
print("M=",M)
print("N=",N)