import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,6],[7,8,9])
plt.xlim(1,5)
plt.ylim(1,6)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Graph Demo")
plt.legend(["values"])
plt.show()