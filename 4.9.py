#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:46:58 2021

@author: nurguliminova
"""

def fahrenheit(c):
    f = (9/5)*c + 32
    return f

def table():
    print('celcius','\t','fahrenheit')
    for i in range(0,101):
        print('{:>7}\t\t{:>10}'.format(i,round(fahrenheit(i),2)))
    

table()