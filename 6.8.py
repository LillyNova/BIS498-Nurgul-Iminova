#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:32:13 2021

@author: nurguliminova
"""


def num_word(number):
    d = { 0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
          6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
          11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
          15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
          19 : 'nineteen', 20 : 'twenty',
          30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
          70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }
    k = 1000
    m = k * 1000
    b = m * 1000
    t = b * 1000

    assert(0 <= number)

    if (number < 20):
        return d[number]

    if (number < 100):
        if number % 10 == 0: return d[number]
        else: return d[number // 10 * 10] + ' ' + d[number % 10]

    if (number < k):
        if number % 100 == 0: return d[number // 100] + ' hundred'
        else: return d[number // 100] + ' hundred ' + num_word(number % 100)

    if (number < m):
        if number % k == 0: return num_word(number // k) + ' thousand'
        else: return num_word(number // k) + ' thousand, ' + num_word(number % k)
    
amount = input()

# Good, but you need a user prompt for the input    -1
arr = amount.split('.')


if len(arr)==2 :
   print(num_word(int(arr[0])).upper(),"AND",arr[1],"/",10**(len(arr[1])))
else :
   print(num_word(int(arr[0])).upper())


   
   