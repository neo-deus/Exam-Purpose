'''24. The set of input is given as ages. Then print the status according to the rules
    using python program.
      Age Status
      <2 in born
      2-10 child
      11-17 young
      18-49 adult
      50-79 old
      >80 very old'''

# solution
n=int(input("Enter the age of person : "))
if n>=0:
  if n<2:
    print("inborn")
  elif n>=2 and n<=10:
    print("child")
  elif n>=11 and n<=17:
    print("young")
  elif n>=18 and n<=49:
    print("adult")
  elif n>=50 and n<=79:
    print("old")
  else:
    print("very old")
else:
  print("invalid age")