#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:43:09 2021

@author: nurguliminova
"""

import numpy as np
array1=np.array([[0,1],[2,3]])
array2=np.array([[4,5],[6,7]])


array3=np.concatenate((array1,array2),axis=0) 
print("Array 3 is \n",array3)
print(" ")

# b)
array4=np.concatenate((array1,array2),axis=1) 
print("Array 4 is \n",array4)
print(" ")

# c)
array5=np.concatenate((array4,array4),axis=0) 
print("Array 5 is \n",array5)
print(" ")

#  d)

array6=np.concatenate((array3,array3),axis=1) 
print("Array 6 is \n",array6)
print(" ")