#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 22:07:00 2021

@author: nurguliminova
"""

PRINCIPAL=1000
INTEREST_RATE=7

# years=10 - 30
for YEARS in range(10,31,1):
    AMOUNT=PRINCIPAL*(1+INTEREST_RATE/100)**YEARS
    
    print("After {} years: ${:.2f}".format(YEARS,AMOUNT))