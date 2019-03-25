#!/usr/bin/python
# import math plotting library 
import matplotlib.pyplot as plt
# create two empty arrays or lists
x = []
y = []
# open file and read it line by line
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

# plot x and y arrays
plt.plot(x, y)
# add xlabel
plt.xlabel('year')
# add ylabel
plt.ylabel('CPI')
# add a title
plt.title('CPI from year 1947')
# add grid lines
plt.grid(True)
# show the graph!
plt.show()
