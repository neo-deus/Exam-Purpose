'''38. Write a Python program using function check whether a number is an Automorphic
 Number or not. In mathematics, an automorphic number is a number whose square
"ends" in the same digits as the number itself. For example, 5 = 25, 6 = 36, 76 =
5776, and 890625 = 793212890625, so 5, 6, 76 and 890625 are all automorphic
numbers.'''

# solution
n=int(input("Enter a number : "))
m=n**2
if str(n) in str(m):
  print("It is an automorphic number")
else:
  print("It is not an automorphic number")
