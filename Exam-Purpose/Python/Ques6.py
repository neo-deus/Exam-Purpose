'''6. Write a python program to find the last position of a substring “Emma” in a given string'''

# solution
s=input("Enter a string : \n")
t='Emma'
print(f"The last position where 'Emma' was found is {s.rfind(t)}")
# w=s.split()
# p=0
# for i in range(len(w)):
#   if(w[i]=="Emma"):
#     p=i
# print("last position where 'Emma' is found is : ",p)