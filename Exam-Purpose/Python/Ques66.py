'''66. Display electricity consumption of a customer for 12 months using suitable
graphical tools.'''

# solution
import matplotlib.pyplot as plt
import random
bill=[]
for i in range(12):
  bill.append(random.randint(1000,2500))
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
plt.plot(month,bill)
plt.xlabel('Month-->')
plt.ylabel('Bill-->')
plt.title('Electricity bill')
plt.show()