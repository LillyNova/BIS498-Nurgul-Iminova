#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:36:34 2021

@author: nurguliminova
"""

import re

# list of months
months = ['January','February','March','April','May','June','July','August','September','October','November','December'] 

text = "date in format 1: 042555, date in format 2: 05/13/1956, date in format 3: August 18, 1954."

print(text)

format1 = re.search("[0-9][0-9][0-9][0-9][0-9][0-9]",text) # finding 6 digits from text

if format1: # if date in format 1 is found

    format1 = format1.group() # grouping the searched format

    f1 = re.findall("[0-9][0-9]",format1) # making list of all 2 digit numbers

    f1month = f1[0] # month

    f1date = f1[1] # date

    f1year = "19"+f1[2] # year
    
    format12 = f1month + "/" + f1date + "/" + f1year # format 2

    format13 = months[int(f1month)-1] + " " + f1date + ", " + f1year # format 3

    print(format1) 
    print(format12) 
    print(format13) 
print()

format2 = re.search("[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]",text) # format 2

if format2: 

    format2 = format2.group() 
    f2 = re.findall("[0-9][0-9]",format2) # making list of all 2 digit numbers

    f2month = f2[0] # month

    f2date = f2[1] #  date

    f2year = f2[2]+f2[3] # year

    format21 = f2month + f2date + f2[3] # format 1

    format23 = months[int(f2month)-1] + " " + f2date + ", " + f2year # format 3

    print(format2)
    print(format21)
    print(format23)
    print()

c=0

for month in months: 

    c = c+1 

    format3 = re.search(month + " [0-9][0-9], [0-9][0-9][0-9][0-9]",text) # searching format 3

    if format3: 
        format3 = format3.group() 
        if c<10: 

            f3month = "0"+str(c) 
        else:

            f3month = str(c) 

        f3 = re.findall("[0-9][0-9]",format3) # making list of all 2 digit numbers

        f3date = f3[0] # date

        f3year = f3[1]+f3[2] # year

        format31 = f3month + f3date + f3[2] # munging into format 1

        format32 = f3month + "/" + f3date + "/" + f3year # munging into format 2

        print(format3)

        print(format31)

        print(format32)