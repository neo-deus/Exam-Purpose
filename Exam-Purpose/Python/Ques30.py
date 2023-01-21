'''30. Write a short program to find the average of some numbers entered through the
keyboard.
Output
Enter numbers (Enter 'q' to see the average)
2 5 7 15 12 q
Average = 8.2'''

# solution
print("Enter numbers (Enter 'q' to see the average) : ")
sum=0
n=0
while True:
  m=input()
  if m=='q':
    avg=sum/n
    break
  else:
    sum+=int(m)
    n+=1
print(f"The average of the given values is {avg}")