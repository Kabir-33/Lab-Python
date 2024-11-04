import matplotlib.pyplot as plt 
x=[1,2,3,4]
e=(0.1,0,0,0)   # 0.1 is used to seperate the pie block
plt.pie(x,explode=e)
plt.title("Pie Chart")
plt.show()