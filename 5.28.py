#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 16:43:25 2021

@author: nurguliminova
"""

# Placing the 20 responses in the list

list = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]


import numpy as np
import statistics

# Display the frequency of each rating

elements, unique = np.unique(list, return_counts=True)
for i in range(len(elements)):
    print('Frequency', elements[i], 'is', unique[i])
    
    
# Diplaying the statistics

print('Min:', min(list))
print('Max:', max(list))
print('Range:', max(list) - min(list))
print('Med:', statistics.median(list))
print('Mod:', statistics.mode(list))
print('Var:', statistics.variance(list))
print('St Dev:', statistics.stdev(list))

