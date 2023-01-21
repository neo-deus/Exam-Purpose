'''18. Write a Python function that accepts a string and calculate the number of upper case
letters and lower case letters. Sample String : ‘The quick Brow Fox’
Expected Output :
No. Of Upper case characters : 3
No. Of Lower case Characters : 12'''

# solution
s=input("Enter a string : ")
c1=0
c2=0
for i in s:
  if i.isupper():
    c1+=1
  elif i.islower():
    c2+=1
print("No. Of Upper case characters : ",c1)
print("No. Of Lower case characters : ",c2)
