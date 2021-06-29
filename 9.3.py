#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 18:48:28 2021

@author: nurguliminova
"""

import csv 
filename = "grades.csv"
def menu():
  
  while True:
    print("--------FILE---------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Exit")
    option = int(input("Enter the option [1 - 3] : "))
    if option >=1 and option <=3:
      break
    print("Invalid option. Enter again.")
  return option

def addStudents():
  
  firstName = input("Enter the first name \t: ")
  lastName = input("Enter the last  name \t: ")
  firstGrade = int(input("Enter the first grade \t: "))
  secondGrade = int(input("Enter the second grade \t: "))
  thirdGrade = int(input("Enter the third  grade \t: "))

  student = [firstName, lastName, firstGrade, secondGrade, thirdGrade]
  
  with open(filename, 'a') as csvfile: 
   
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(student)

def displayStudents():

  fields = [] 
  rows = [] 
  
  with open(filename, 'r') as csvfile: 
    
    csvreader = csv.reader(csvfile) 

    fields = next(csvreader) 
  
    for row in csvreader: 
      rows.append(row) 

  print(f"Total no. of students :{csvreader.line_num - 1}") 

  print("-"*76)
  print(f"| {fields[0]:12} | {fields[1]:12} | {fields[2]:12} | {fields[3]:12} | {fields[4]:12} |")
  print("-"*76,end = "")
  for row in rows: 
    
    print("\n| ",end = "")
    for col in row: 
      print(f"{col:12} | ",end= "")
  print("\n"+"-"*76)

def main():
  fields = ['FirstName', 'LastName', 'Pass1Grade','Pass2Grade','Pass3Grade']
 
  with open(filename, 'w') as csvfile: 
    
    csvwriter = csv.writer(csvfile) 
    
    csvwriter.writerow(fields) 
  while True:
    option = menu()
    if option == 3:
      break
    if option == 1:
      addStudents()
    else:
      displayStudents()
main()