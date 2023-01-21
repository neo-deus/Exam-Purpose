'''35. Python program to check if a string has at least one letter and one number
Examples:
Input: welcome2ourcountry34
Output: True
Input: stringwithoutnum
Output: False'''

# solution
s=input("Enter a string : ")
num=False
alpha=False
for i in s:
  if i.isdigit():
    num=True
  elif i.isalpha():
    alpha=True
if num==True and alpha==True:
  print("True")
else:
  print("False")
