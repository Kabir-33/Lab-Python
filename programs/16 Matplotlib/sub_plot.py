import matplotlib.pyplot as plt
import numpy as np

# Part 1
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("Sales")

# Part 2
x=np.array([0,1,2,3])
y=np.array([0,10,20,30])
plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("Income")
plt.suptitle("My Shop")
plt.show()
 