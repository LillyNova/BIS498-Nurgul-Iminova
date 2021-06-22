#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:20:16 2021

@author: nurguliminova
"""

import numpy as np


print('\nFlattened()')
a = np.array([[1, 2, 4], [8, 16, 32]])
print('Original array:\n', a)
b = a.flatten()
print()
b[1] = 0
print('Original array with changes in flattened array:\n', a)


 
print('\n\nRavel()')
x = np.array([[1, 2, 4], [8, 16, 32]])
print('Original array:\n', x)
y = x.ravel()
print()
y[1] = 0
print('Original array with changes in flattened array:\n', x)
 