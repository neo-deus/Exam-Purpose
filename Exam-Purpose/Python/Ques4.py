'''4. A store charges Rs.120 per item if you buy less than 10 items. If you buy between 10
      and 99 items, the cost is Rs.100 per item. If you buy 100 or more items, the cost is
      Rs.70 per item. Write a program that asks the user how many items they are buying
      and prints the total cost.'''

# solution
a=int(input("Enter the number of items: "))
if a>=0:
  if a<10:
    total=a*120
  elif a>=10 and a<100:
    total=a*100
  else:
    total=a*70
  print(f"Total cost of items is {total}")
else:
  print("Invalid number of items")

