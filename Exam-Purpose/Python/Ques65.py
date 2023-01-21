'''65. Election results of India for the year 2000 is published. Out of 400 seats 'ABC' got 180, 'XYZ' got 200 and 'MNP' got rest. Display the result using suitable graphical
tools.'''

#solution
import matplotlib.pyplot as plt
import numpy as np
y = np.array([180,200,20])
mylabels = ["ABC", "XYZ", "MNP"]
plt.pie(y, labels = mylabels)
plt.show()