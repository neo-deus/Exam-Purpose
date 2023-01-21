'''58.Write a program to compare two equal sized lists and print the first index where they differ.'''

# solution
l1=[2,5,7,9,1,4,9,5,3,2,1]
l2=[2,5,7,9,1,4,9,5,3,2,1]
if len(l1) != len(l2):
  print("Unequal lists")
else:
  i=0
  flag=True
  for i in range(len(l1)):
    if l1[i] != l2[i]:
      flag=False
      break
  if flag==False:
    print(f"The lists differ at index {i}")
  else:
    print("The lists are identical")