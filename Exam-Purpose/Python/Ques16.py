'''16. Write a Python function to check whether a string is a pangram or not. Pangrams are
words or sentences containing every letter of the alphabet at least once.
For example : “The quick brown fox jumps over the lazy dog”'''

# solution
s='abcdefghijklmnopqrstuvwxyz'
m=input("Enter a string : ")
flag=True
for i in s:
  if i in m.lower():
    pass
  else:
    flag=False
if flag==True:
  print("It is a pangram")
else:
  print("It is not a pangram")
