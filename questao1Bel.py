#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 09:20:14 2017

@author: dan
"""
import matplotlib.pyplot as plt
import numpy as np
import csv

with open('etnia.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    header = next(reader, None)
    content = list(reader)

#print(reader)
print(header)
#print(content)