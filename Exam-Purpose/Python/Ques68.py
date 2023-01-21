'''68. Display the marks of two students for 5 subjects using suitable graphical tools. '''

# solution
import matplotlib.pyplot as plt
student1_marks = [85, 67, 88, 72, 60]
student2_marks = [70, 80, 75, 91, 85]
x = [1, 2, 3, 4, 5]
width = 0.35
marks=["Maths","Chemistry","Physics","English","Computer"]
plt.bar(x, student1_marks, width, label='Student 1')
plt.bar([i+width for i in x], student2_marks, width, label='Student 2')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.xticks(x,marks)
plt.title('Marks of two students')
plt.legend()
plt.show()