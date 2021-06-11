#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:13:34 2021

@author: nurguliminova
"""

verse = ('“How many slams in an old screen door?'
'Depends how loud you shut it.'
'How many slices in a bread?'
'Depends how thin you cut it.'
'How much good inside a day?'
'Depends how good you live them.'
'How much love inside a friend?'
'Depends how much you give them.')

verse1 = verse.upper()

count_words = {}


for word in verse1.split():
   if word in count_words:
        count_words[word] += 1
   else:
        count_words[word] = 1
        count_words[word] = 1
    
print('\nUnique words: ',len(count_words) )


print("Duplicate words: ")

for word, count in count_words.items():
    if count_words[word] > 1:
        print(f'{word:<20}')
        
        
        
        