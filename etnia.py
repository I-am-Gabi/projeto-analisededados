#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

"""
import matplotlib.pyplot as plt
import numpy as np
import csv

header = []
content = []
total = []

with open('dadosEtnicos.csv', newline='', encoding='utf_8') as f: 
    reader = csv.reader(f) 
    for row in reader:
    	line = row[0].split(';')
    	header.append(line[0:1][0])
    	l = []
    	for cell in line[1:]:
    		l.append(cell)  
    	content.append(l)
    	if (l[-1] != 'Total'):
    		total.append(float(l[-1]))


#print(total)
#print(header[1:])
plt.bar([0, 1, 2, 3, 4, 5, 6, 7],  total,0.5, align='center')
#plt.xticks(total, header[1:])
plt.yticks([0, 1, 2, 3, 4, 5, 6, 7], header[1:])
#plt.legend(handles=[red,green,blue])
plt.show()
#print(content)


    