'''28. Write programs using nested loops to produce the following patterns:
        A
        A B
        A B C
        A B C D
        A B C D E
        A B C D E F'''

s='ABCDEF'
n=len(s)
for i in range(1,n+1):
  for j in range(i):
    print(s[j],end=" ")
  print()