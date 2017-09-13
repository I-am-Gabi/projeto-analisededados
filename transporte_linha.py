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

with open('meio_transporte.csv', newline='', encoding='utf_8') as f: 
    reader = csv.reader(f) 
    for row in reader:
    	line = row[0].split(';')
    	header.append(line[0:1][0])
    	l = []
    	for cell in line[1:]:
            if cell.isdigit():
                l.append(int(cell))  
            else:
                l.append(cell)
    	content.append(l)


etnias = ['Coletivo', 'Veiculo próprio', 'Outro', 'Não se aplica', 'Não respondeu']#header[1:]

for x in range(1, 9):
    #print(etnias[x-1], content[x][:-1]) 
    plt.plot(range(len(content[x][:-1])), content[x][:-1], linestyle='--', label='%s' % etnias[x-1])

plt.ylabel('matriculas')
plt.xlabel('anos')
plt.legend() 

plt.show()