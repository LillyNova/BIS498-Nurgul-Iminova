#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:59:21 2021

@author: nurguliminova
"""


# importing library

from random import randint

# creating list

game_board = []
lst = []
rows_letters = "abcdefghij"

# Building 10 x 10 board

def build_game_board(board):
    for item in range(10):
        board.append(["O"] * 10)

def show_board(board):
    print("Welcome to the battleship game!")
    for row in board:
        print(" ".join(row))

# Waiting for the input

input(" ")
answer = input ('Enter N or H \n')
if answer == 'N':
    print ('Play again. Enter N or H now \n')
else:
    print ('You sank their battleship!')
    
# Error checking

if answer !='N' or answer!='H':
    print ('Error! Enter N or H')
else: 
   
