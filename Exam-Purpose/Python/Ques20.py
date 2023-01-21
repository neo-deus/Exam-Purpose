'''20. Given a list of integers, write a program to find those which are palindromes.'''

# solution
l=[2,8,44,54,334,90,121,17,99]
def palindrome(v):
  dup=v
  s=0
  while dup>0:
    s=s*10+(dup%10)
    dup=dup//10
  if s==v:
    print(v,end=' ')
print("The palindrome numbers in the given list are : ")
for i in l:
  palindrome(i)