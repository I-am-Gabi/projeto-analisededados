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
            
x_name = ['Branco(a)', 'Negro(a)', 'Amarelo(a)', 'Pardo(a)', 'Indígena', 'Quilombo', 'Não se aplica', 'Não respondeu']#header[1:]
x = np.arange(len(x_name))
plt.bar(x, total)  
plt.xticks(x, x_name, rotation=30, fontsize=8) 


plt.xlabel('Etnias')
plt.ylabel('N° de inscritos')
plt.title('Etnias dos alunos matriculados no ano de 2013')

plt.show() 


    