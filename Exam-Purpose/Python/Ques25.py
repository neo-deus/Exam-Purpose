'''25. Write a program to accept the age of n employees and count the number of persons
in the following age group: (i) 26 - 35 (ii) 36 - 45 (iii) 46 - 55'''

# solution
n=int(input("Enter the number of employees : "))
l=[]
c1=c2=c3=0
print("Enter the ages : ")
for i in range(n):
  m=int(input())
  l.append(m)
for i in l:
  if i>=26 and i<=35:
    c1+=1
  elif i>=36 and i<=45:
    c2+=1
  elif i>=46 and i<=55:
    c3+=1
print(f"The no. of employees aged 26-35 is {c1},the no. of employees aged 36-45 is {c2} and the no. of employees aged 46-55 is {c3}")