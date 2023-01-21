'''64. Take the five marks of a student for a particular subject. Display the data
graphically using suitable graph.'''

# solution
import matplotlib.pyplot as plt
marks = [85, 75, 90, 80, 60]
x = ['Exam 1','Exam 2','Exam 3','Exam 4','Exam 5']
plt.bar(x, marks)
plt.xlabel('Subject - Physics')
plt.ylabel('Marks')
plt.title('Marks of a student')
plt.show()