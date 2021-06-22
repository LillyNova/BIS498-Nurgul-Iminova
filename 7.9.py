#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:22:49 2021

@author: nurguliminova
"""

import numpy as np
'''create array'''
arr= np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
'''reshape array'''
arr=np.reshape(arr, (3, 5))
print (arr)

'''select row 2'''
x=arr[2:3, :]
print("Row 2 is :",x)

'''select column 4'''
x=arr[:,4:5]
print("\ncolumn 4 is\n",x)

'''select rows 0 and 1'''
x=arr[:2,:]
print("\nrows 0 and 1 is\n",x)

'''select column 2-4 '''
x=arr[:,2:5]
print("\ncolumn 2-4 is\n",x)

'''select row 1 and column 4'''
x=arr[:1,[4]]
print("\nselect rows 1 and column 4\n",x)

'''select from rows 1 and 2 that are in column 0,2,4'''
x=arr[1:3,[0,2,4]]
print("\nselect rows 2:3 and colums 0,2,4\n",x)

