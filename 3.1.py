#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:20:00 2021

@author: nurguliminova
"""

# initialize variables
passes = 0 # number of passes
failures = 0 # number of failures
# process 10 students
for student in range(10):
    # get one exam result
    result = int(input('Enter result (1=pass, 2=fail):'))
    while result != 1 and result != 2:
        print('Invalid Result!')
        result = int(input('Enter result (1=pass, 2=fail): '))
    if result == 1:
        passes = passes + 1
    else:
        failures = failures + 1
# termination phase
print('Passed:', passes)
print('Failed:', failures)
if passes > 8:
    print('Bonus to instructor')