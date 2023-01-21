'''13. Write a python program to reduce a string of lowercase characters in range ascii [‘a’..’z’] by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them. Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String.
Input- aaabccddd, output-abd,
Input- abba, output-empty string.'''

# solution
s=input("Enter a string : ")
v=[]
for i in range(len(s)):
  if v==[]:
    v.append(s[i])
  elif s[i] != v[len(v)-1]:
    v.append(s[i])
  else:
    v.pop()
a=""
for i in range(len(v)):
  a=a+v[i]
if a != "":
  print(a)
else:
  print("Empty string")