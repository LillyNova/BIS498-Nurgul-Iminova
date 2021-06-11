#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 11:50:55 2021

@author: nurguliminova
"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
# a
f_half = int(len(alphabet)/2)

print(alphabet[0:f_half])

#b
print(alphabet[:f_half])

#c
s_half = len(alphabet)
print(alphabet[f_half:s_half])

#d
print(alphabet[f_half:])

#e
print(alphabet[::2])

#f
print(alphabet[::-1])

#g
reverse=alphabet[::-1]
print(reverse[::3])