import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)

plt.clf()
plt.hist(data, bins=20, color='skyblue', edgecolors='black')
plt.title("Histogram Chart")

plt.xlabel("values")
plt.ylabel("Frequency")
plt.show()

import matplotlib.pyplot as plt

labels =['English', 'Math', 'Science', 'History']
sizes = [45, 30, 15, 10]

plt.clf()
plt.pie(sizes, lavels=lavels, autopct='%1.1f%%',
        startangle=140,colors=['lightblue', 'lightgree',
                               'lightcoral', 'lightsalmon'])
plt.title("Subjects Distribution")
plt.show()