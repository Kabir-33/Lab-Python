# 7. Python program to display a horizontal bar chart of the popularity of programming Languages.
#  Sample data: Programming languages: Java, Python, PHP, JavaScript, C#, C++ 
#  Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularity')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

plt.show()
