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
    		l.append(cell)  
    	content.append(l)
    	if (l[-1] != 'Total'):
    		total.append(float(l[-1]))

x = np.arange(len(header[1:]))
x_name = ['Coletivo', 'Veículo próprio', 'Outro', 'Não se aplica', 'Não respondeu'] #header[1:]
plt.bar(x, total)  
plt.xticks(x, x_name) 


plt.xlabel('Meios de transporte')
plt.ylabel('N° de inscritos')
plt.title('Meios de transporte dos alunos matriculados no ano de 2013')

plt.show() 


    