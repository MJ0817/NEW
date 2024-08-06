
#시간대별 습도 그래프 만들기


import matplotlib.pyplot as plt

# x와 y 배열의 길이 맞추기 (y 배열에 요소 하나 추가)
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
y = [85, 90, 90, 90, 90, 90, 90, 85, 85, 80, 75, 80, 75, 70, 70, 65, 60, 70, 80, 90, 90, 90, 90, 95]  # y에 100을 추가하여 길이 맞추기

plt.plot(x, y, marker='*', linestyle='-', color='red', label='temp')
plt.title("Daily Humidity Trend")
plt.xlabel("Time (Hour)")
plt.ylabel("Humidity (%)")
plt.legend()
plt.grid(True)
plt.show()


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

labels = ['English', 'Math', 'Science', 'History']
sizes = [45, 30, 15, 10]

plt.clf()
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        startangle=140,colors=['lightblue', 'lightgreen',
                               'lightcoral', 'lightsalmon'])
plt.title("Subjects Distribution")
plt.show()