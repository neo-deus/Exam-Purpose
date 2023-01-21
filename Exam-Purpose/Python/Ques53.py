'''53.Create the following lists using a for loop:
The list ['a','bb','ccc','dddd', . . . ] that ends with 26 copies of the letter z.'''

# solution
s='abcdefghijklmnopqrstuvwxyz'
l=[]
for i in range(len(s)):
  t=""
  for k in range(i+1):
    t+=s[i]
  l.append(t)
print(l)
