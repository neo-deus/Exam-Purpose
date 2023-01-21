'''40. Write a program to calculate the amount payable after simple and compound interest.'''

# solution
p=float(input("Enter the principal amount : "))
r=float(input("Enter the rate of interest : "))
t=float(input("Enter the no. of years : "))
si=p*r*t/100
ci=p*((1+r/100)**t)
print(f"The total amount using simple interest will be {si+p}")
print(f"The total amount using compound interest will be {ci}")