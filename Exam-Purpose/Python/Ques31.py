'''31. Python program to capitalize the first and last character of each word in a string
Input: hello world
Output: HellO WorlD'''

# solution
s=input("Enter a string : ")
w=s.split()
t=""
for item in w:
  t+=item[0].upper()+item[1:-1]+item[-1].upper()+" "
print("Input : ",s)
print("Output : ",t)