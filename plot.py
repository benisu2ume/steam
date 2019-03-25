#!/usr/bin/python
# import math plotting library 
import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import polyfit
# create two empty arrays or lists
x = []
y = []
# open data file and read it line by line
with open('data/cu.data.1.AllItems.M01.CUSR0000SA0', 'r') as cpi_file:
	# for each line in the file
    for line in cpi_file:
    	# split each line into an array by spaces
    	d = line.split()
    	# year is the 2nd element or index 1
    	year = float(d[1])
    	# cpi is the 4th element or index 3
    	cpi = float(d[3])
    	x.append(year)
    	y.append(cpi)
# get offset and slope with polyfit
b, m = polyfit(x, y, 1)
# get value at 2069
l_end = b + m*2069
f = []
l = []
for i in range(1947,2080):
	l.append(float(i))
	f.append(b + m*i)
# plot x and y arrays
plt.plot(x, y, label='BLS CPI data')
plt.plot(l, f, '-', label='estimated CPI')
# add point for 2069
plt.plot(2069, l_end, 'ro')
plt.text(2069, l_end , 'CPI: %.2f'%(l_end), bbox=dict(facecolor='yellow', alpha=0.2), fontsize=10)
# add xlabel
plt.xlabel('year')
# add ylabel
plt.ylabel('CPI')
# add a title
plt.title('CPI from year 1947 to 2069')
# add grid lines
plt.grid(True)
# show legend
plt.legend()
# show the graph!
plt.show()
