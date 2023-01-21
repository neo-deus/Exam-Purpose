'''52.A student's grade is calculated in a subject according to the following rules:
        Number          Obtained Grade
        >=90 and <=100        O
        >=80 and <90          E
        >=70 and <80          A
        >=60 and <70          B
        >=50 and <60          C
        >=40 and <50          D
        <40 and >=0        F(FAILED)
        Others No.          INVALID
Write a Python script which accept a student's marks as an input and then
determine the grade of the students in that subject. Do this program using 'if-else-if' statement'''

# solution
n=int(input("Enter the marks of the student : "))
if n>=0 and n<=100:
  if n>=90:
    print("Ontained grade - O")
  elif n>=80:
    print("Ontained grade - E")
  elif n>=70:
    print("Ontained grade - A")
  elif n>=60:
    print("Ontained grade - B")
  elif n>=50:
    print("Ontained grade - C")
  elif n>=40:
    print("Ontained grade - D")
  else:
    print("Ontained grade - F")
else:
  print("Invalid grade")