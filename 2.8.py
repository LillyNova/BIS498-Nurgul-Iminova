#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:19:42 2021

@author: nurguliminova
"""

first = int(input("First integer:\t"))
final = int(input("Final integer:\t"))

print ('number')
for number in range (0,6):
    print (number)
    
print ('\nsquare')


def printTable(first,final):
    result = 1
    for x in range(first, final):
        print(x, x ** 2, x ** 3)

printTable(first, final)