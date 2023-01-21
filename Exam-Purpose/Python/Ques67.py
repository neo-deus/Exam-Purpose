'''67. Plot the curve O(n) and O(n^2).'''

# solution
import matplotlib.pyplot as plt
import numpy as np
plt.xlabel("x-axis")
plt.ylabel("y-axis")
x=np.arange(1,25,1.0)
y1=x
y2=x**2
plt.plot(x,y1,color="blue",linestyle="dotted",label="O(n)")
plt.plot(x,y2,color="red",linestyle="dashed",label="O(n2)")
plt.legend()
plt.show()