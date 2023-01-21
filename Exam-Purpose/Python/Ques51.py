'''51.Write a Python script to create Simple Calculator on user choice.'''

# solution
n1=int(input("Enter first number : "))
n2=int(input("Enter second number : "))
c=input("Enter + for sum, - for subtract, * for multiply, / for divide, '%' for remainder : ")
match c:
  case '+': 
    print(f"The result is {n1+n2}")
  case '-':
    print(f"The result is {n1-n2}")
  case '*':
    print(f"The result is {n1*n2}")
  case '/':
    print(f"The result is {n1/n2}")
  case '%':
    print(f"The result is {n1%n2}")
  case default:
    print("Invalid option")