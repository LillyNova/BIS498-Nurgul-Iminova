#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:32:13 2021

@author: nurguliminova
"""


def number_to_word(num):
    l = len(num);
    if (l == 0):
       print("Empty");
       return;
    if (l > 4):
       print("Length more than 4 is not supported");
       return;
       

    ones = ["zero", "one", "two", "three", "four", 
            "five", "six", "seven", "eight", "nine"];
    twos = ["", "ten", "eleven", "twelve", "thirteen", "fourteen", 
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];
    tens = ["", "", "twenty", "thirty", "forty", "fifty", 
            "sixty", "seventy", "eighty", "ninety"];
    thou = ["hundred", "thousand"];

    if (l == 1):
        print(ones[ord(num[0]) - '0']);
        return;
    x = 0;
    while (x < len(num)):
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(ones[ord(num[x]) - 48],
                                           end = " ");
                print(tens[l - 3], end = " ");  
            l -= 1;
        else:
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                   ord(num[x+1]) - 48);
                print(twos[sum] , end = " ");
                return;

            elif (ord(num[x]) - 48 == 2 and
                ord(num[x + 1]) - 48 == 0):
                print("twenty", end = " ");
                return;
       
            else:
                i = ord(num[x]) - 48;
                if(i > 0):
                    print(tens[i], end = " ");
                else:
                    print("", end = "");
                x += 1;
                if(ord(num[x]) - 48 != 0):
                    print(ones[ord(num[x]) - 48], end = " ");
        x += 1;
        
    digit = input("Number : ")
    number = digit.split('.')
    number_to_word(amount_num[0]);

    if(len(number[1]) == 1):
            print("and "+ number[1] + '0/100')
    else:
            print("and "+ number[1] + '/100')