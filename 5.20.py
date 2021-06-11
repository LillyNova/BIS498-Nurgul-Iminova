#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:39:59 2021

@author: nurguliminova
"""


display_table = [ [50,43,61] ,[7,2,9], [15,71,23]]
print(display_table[0])
print(display_table[1])
print(display_table[2])


import pandas as pd
display_table = [[5,8,9], [31,42,89], [8,3,2]]
pd.DataFrame(display_table, columns=["Column 1", "Column 2", "Column 3"])