'''21. Print the following pattern using Python program
        1
        2 1
        4 2 1
        8 4 2 1
        16 8 4 2 1
        32 16 8 4 2 1
        64 32 16 8 4 2 1'''

# solution
n=int(input("Enter the size of pattern : "))
for i in range(1,n+1):
  for j in range(1,i+1):
    print(pow(2,i-1),end=' ')
    i-=1
  print()