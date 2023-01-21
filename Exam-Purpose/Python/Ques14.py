'''14. Write a program to take N (N > 20) as an input from the user. Print numbers from
11 to N. When the number N is a multiple of 3, print "Tipsy", when it is a multiple of 7,
print "Topsy". When it is a multiple of both, print "TipsyTopsy"'''

# solution
n=int(input("Enter a number greater than 20 : "))
for i in range(11,n+1):
    print(i,end=" ")
print()
if n%3==0 and n%7==0:
    print("TipsyTopsy")
elif n%3==0:
    print("Tipsy")
elif n%7==0:
    print("Topsy")