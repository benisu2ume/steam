#!/usr/bin/python

print('here is my plot')
import matplotlib.pyplot as plt
x = [1,2,3]
y = [2,4,2]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('My first graph is cool!')
plt.show()
