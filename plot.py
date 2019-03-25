#!/usr/bin/python
# ----------------------------------------------------------
# imports
# ----------------------------------------------------------
# import math plotting library 
import matplotlib.pyplot as plt
# ----------------------------------------------------------
# read in actual data
# ----------------------------------------------------------
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
# ----------------------------------------------------------
# get the difference year over year
# ----------------------------------------------------------
i = 0
diff = []
last_cpi = 0.0
for cpi in y:
	i += 1
	if i > 1:
		i_diff = ((cpi-last_cpi)/ (float(last_cpi)))
		diff.append(i_diff)
	last_cpi = cpi
# ----------------------------------------------------------
# calculate the average difference
# ----------------------------------------------------------
avg_diff = sum(diff) / (float(len(diff)))
# ----------------------------------------------------------
# extrapolate new line based on average diff
# ----------------------------------------------------------
x2 = []
y2 = []
last = y[len(y) - 1]
yoy = (avg_diff + 1.0)
for i in range(2020, 2070):
	x2.append(float(i))
	new_cpi = last*yoy
	y2.append(new_cpi)
	last = new_cpi
# ----------------------------------------------------------
# plot x and y arrays
# ----------------------------------------------------------
plt.plot(x, y, label='BLS CPI data')
plt.plot(x2, y2, '-', label='estimated CPI')
# ----------------------------------------------------------
# get value at 2019
# ----------------------------------------------------------
l_rend = y[len(y)-1]
# add point for 2019
plt.plot(2019, l_rend, 'bo')
plt.text(2019, l_rend , 'CPI: %.2f'%(l_rend), bbox=dict(facecolor='yellow', alpha=0.2), fontsize=10)
# ----------------------------------------------------------
# get value at 2069
# ----------------------------------------------------------
l_xend = y2[len(y2)-1]
# add point for 2069
plt.plot(2069, l_xend, 'ro')
plt.text(2069, l_xend , 'CPI: %.2f'%(l_xend), bbox=dict(facecolor='yellow', alpha=0.2), fontsize=10)
# ----------------------------------------------------------
# annotate graph
# ----------------------------------------------------------
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
