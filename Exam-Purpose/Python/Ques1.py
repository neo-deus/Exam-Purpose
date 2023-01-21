'''1. Use string slicing to perform the following:
      a. Take a string of length greater than 2, return a string except 1st and last characters.
      b. Take 2 strings, s1, and s2 return a new string made of the first, middle and last char of each input string.
      c. Write a python program to take 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.'''

# a. solution
# while True:
#   s=input("Enter a string: ")
#   if(len(s)>2):
#     print(s[1:len(s)-1])
#     break
#   else:
#     print("Please enter a string of length greater than 2")

# b. solution
s=input("Enter string 1 : ")
t=input("Enter string 2 : ")
v=s[0]+s[len(s)//2]+s[len(s)-1]+t[0]+t[len(t)//2]+t[len(t)-1]
print(v)

# c. solution
# s=input("Enter string 1 : ")
# t=input("Enter string 2 : ")
# v=s[:int(len(s)/2)]+t+s[int(len(s)/2):]
# print(v)