'''23. Write a python program to convert a decimal number to a number of a given base b.'''

# solution
n=int(input("Enter a decimal number : "))
m=int(input("Enter the base in whih you want to convert : "))
dup=n
s=""
if m>1:
  while dup>0:
    if dup%m==10:
      s=s+'A';
    elif dup%m==11:
      s=s+'B';
    elif dup%m==12:
      s=s+'C';
    elif dup%m==13:
      s=s+'D';
    elif dup%m==14:
      s=s+'E';
    elif dup%m==15:
      s=s+'F';
    else:
      s=s+str(dup%m)
    dup=dup//m
  print(s[::-1])
else:
  print("Invalid base")