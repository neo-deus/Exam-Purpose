'''5. Write a python program to find all occurrences of “India” in given string ignoring the case.'''

# solution
s=input("Enter a string : \n")
c=0
w=s.lower().split(" ")
# print(w)
for item in w:
  if item=='india':
    c+=1
print(f"The word 'India' comes for a total of {c} times irrespective of the case.")
