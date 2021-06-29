#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:23:54 2021

@author: nurguliminova
"""

def Latinpig(string):
    LatinpigSuffix = 'ay'
    if len(string) > 0 and string.isalpha():
        word = string.lower()
        first = word[0]
        if first == ('a' or 'e' or 'i' or 'o' or 'u'):
            ay_word = word + LatinpigSuffix
            return ay_word
        else:
            ay_word = word[1:] + first + LatinpigSuffix
            return ay_word
    else:
        return 'empty'
  

def convert(lst):
    return ' '.join(lst)
  
def main():
    str = input("Enter a string input : ");
    lis = str.split(" ")
    out = []
    for strng in lis:
        out.append(Latinpig(strng))
    print(convert(out))    