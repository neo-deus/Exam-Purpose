'''37. Python program to check if a given string is binary string or not
Examples:
Input: str = "01010101010"
Output: Yes'''

# solution
s=input("Enter a binary string : ")
flag=True
for i in s:
  if i=='0' or i=='1':
    pass
  else:
    flag=False
    break
if flag==True:
  print("Yes it is a binary string")
else:
  print("No it is not a binary string")