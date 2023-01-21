'''36.Remove all duplicates characters from a given string in Python
Examples:
Input : abcabcde
Output : abcde'''

# solution
s=input("Enter a string : ")
t=""
for i in s:
  if i not in t:
    t+=i
print("Input : ",s)
print("Output : ",t)