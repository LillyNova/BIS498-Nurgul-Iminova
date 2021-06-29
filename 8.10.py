#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:36:04 2021

@author: nurguliminova
"""
# openinng file and reading it to add to the words list list
def read_file(hachiko):
   file = open("hachiko","r")
   words_list=[]
   for words in file:
       words_list.append(words.strip()) 
   return words_list

if __name__=="__main__":
   positive_word_list = []
   negative_word_list = []
   positive_sentence_count = 0
   negative_sentence_count = 0
   positive_word_list = read_file("PositiveWords.txt")
  
  # Reading from NegativeWords.txt and saving in negative_words list
   negative_word_list = read_file("NegativeWords.txt")

   h = open("hachiko.txt","r")
  
   #Starting a loop to read line by line and find sentiment of line
  
   for sentence in h:
       #getting list of words out of the sentence
       #split() will return list of words separated by spaces
       words_list = sentence.split() 
       
       pos_word_count =0
       neg_word_count =0
       
       #counting no of respective mood words
       for words in words_list:
           if words in positive_word_list:
               pos_word_count+=1
           elif words in negative_word_list:  
               neg_word_count+=1
           else:
             
               pass

       #Condition for positive sentence
       if(pos_word_count>neg_word_count):  
           positive_sentence_count+=1
      
       #Condition for negative_sentence_count
       elif(pos_word_count<neg_word_count):
           negative_sentence_count+=1
           


  # printing number of words
   print("Positive: ",positive_sentence_count)
   print("Negative: ",negative_sentence_count)
