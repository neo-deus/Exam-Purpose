'''15. Write a Python program that accepts a hyphen-separated sequence of words as
input and prints the words in a hyphen-separated sequence after sorting them
alphabetically.
Sample Input : green-red-yellow-black-white
Output : black-green-red-white-yellow'''

# solution
s=input("Enter a hyphen-separated sequence : ")
w=s.split('-')
w.sort()
for i in range(len(w)-1):
  print(w[i],end='-')
print(w[len(w)-1])