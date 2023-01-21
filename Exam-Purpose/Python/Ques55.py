'''55.Write programs as per following specifications: Print the length of the
longest string in the list of strings str_list. Precondition : the list will contain
at least one element.'''

# solution
str_list=['sdfh','iuwery','mnb','aueghakse','zmxcbn','lsadkfh','opiweut']
max=0
s=""
for i in str_list:
  a=len(i)
  if a>max:
    max=a
    s=i
print(f"The longest string is '"+s+f"' and it's length is {max}")