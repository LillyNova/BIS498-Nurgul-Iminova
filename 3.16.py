#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:44:10 2021

@author: nurguliminova
"""

numbers = list(map(int, input().split()))
FLargest = -1
SLargest = -1

for n in values:
   if n > FLargest:
        FLargest = n
        
for n in numbers:
    if n > SLargest:
        if n != FLargest:
            SLargest = n

print("First Largest:", FLargest)
print("Second Largest:", SLargest)