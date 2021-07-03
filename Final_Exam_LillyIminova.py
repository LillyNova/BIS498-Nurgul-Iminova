#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 00:34:24 2021

@author: nurguliminova
"""

import pandas as pd

# reading csv file

wm=pd.read_csv('WMT.csv')

# exploring the data

wm

wm.head(10)

wm.tail(10)

wm.describe()

wm.info()

# memory usage check

wm.memory_usage(index=False)

#finding out the data type of Adj Close
wm['Adj Close'].dtypes

wm['Adj Close'].head(5)

#understanding the format of the Date column
wm['Date'].describe()

# converting column Date from object into readable format
wm.set_index('Date', inplace=True)

wm.head (10)

# Calculation of return this month in accordance with the formula
wm['Returns_t-1'] = wm['Adj Close'].shift(1)

wm['Returns_t-1'].head()

wm.head(5)

wm['monthly_return']=wm['Adj Close']/wm['Returns_t-1']-1

wm.head(5)

# dropping the first row
wm = wm.drop(wm.head(1).index)
wm

#importing libraries

import matplotlib as mpl
import matplotlib.pyplot as plt

# Drawing a plot

wm['monthly_return'].plot(figsize=(12,8))

plt.ylabel('monthly_return')
plt.xlabel('Date')
plt.show()

wm.describe()

#Finding the month of highest average return

wm_max = wm[wm.monthly_return == wm.monthly_return.max()]
wm_max

# Based on the analysis, the month with the highest average return is October 1st, 1998


# Saving altered data set

wm.to_csv('WM_final.csv', index = False)

