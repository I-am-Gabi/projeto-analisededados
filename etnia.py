#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""

"""
import matplotlib.pyplot as plt
import numpy as np
import csv

header = []
content = []

with open('dadosEtnicos.csv', newline='', encoding='utf_8') as f: 
    reader = csv.reader(f) 
    for row in reader:
    	line = row[0].split(';')
    	header.append(line[0:1][0]) 
    	for cell in line[1:]:
    		content.append(cell)  


print(header)
print(content)


    