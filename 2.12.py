#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:08:41 2021

@author: nurguliminova
"""

PRINCIPAL=1000
INTEREST_RATE=7

for N in range(10,31,10):
    AMOUNT=PRINCIPAL*(1+INTEREST_RATE/100)**N
    
    print("After {} years: ${:.2f}".format(N,AMOUNT))