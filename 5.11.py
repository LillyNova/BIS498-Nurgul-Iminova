#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 12:25:14 2021

@author: nurguliminova
"""

def summarize_letters(string):
    l_counter = {}
    l_lower = string.lower()
    for i in l_lower:
        if i in l_counter and i.isalpha():
            l_counter[i] = l_counter[i] + 1
        if i not in l_counter and i.isalpha():
            l_counter[i] = 1
    tuples = [(a, b) for a, b in l_counter.items()]
    return tuples

letters = 'a s d f F g H j k L p p O I u y t r E W W q Z x c v B n m H D Y u u k L L E H I H G u n i v e r s i t y'
print(summarize_letters(letters))
import string
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet = set(string.ascii_lowercase)
if set(letters.lower()) >= alphabet:
    print('The string ' + letters +' has all the letters of the alphabet ')