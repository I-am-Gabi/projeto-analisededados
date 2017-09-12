#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:20:14 2017

@author: dan
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

header = []
content = []

with open('etnia.csv', newline='', encoding='utf_8') as f: 
    reader = csv.reader(f) 
    for row in reader:
    	header.append(row[0:1][0])
    	print(row[1:])
    	#content.append(row[1:])
    


#print(reader)
#print(header)
#print(content[0])