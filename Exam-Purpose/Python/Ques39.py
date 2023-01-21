'''39. Say a box of cookies can hold 24 cookies, and a container can hold 75 boxes of
cookies. Write a program that prompts the user to enter the total number of cookies,
then outputs the number of boxes and the number of containers to ship the cookies.
Note that each box must contain the specified number of cookies, and each
container must contain the specified number of boxes. If the last box of cookies
contains less than the number of specified cookies, you can discard it and output
the number of leftover cookies. Similarly, if the last container contains less than the
number of specified boxes, you can discard it and output the number of leftover
boxes.'''

# solution
n=int(input("Enter the total no. of cookies : "))
box=n//24
leftbox=n%24
cont=box//75
leftcont=box%75
print(f"The total number of containers are : {cont}\nThe total number of leftover boxes are : {leftcont}\nThe total number of leftover cookies are : {leftbox}")