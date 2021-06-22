#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:18:57 2021

@author: nurguliminova
"""

array1 = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
array2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]


for i in range(3):
    for j in range(3):
        array1[i][j] = array1[i][j] * array2[i][j]

print(array1)