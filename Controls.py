# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 17:00:15 2018

@author: Hamza

simple program to demonstrate if, elif and else statements. As well as for loop.

"""

age = input("How old are you?\n")                                               # age variable, asks for user input. Recieves input as a string
age = int(age)                                                                  # casts age variable from a string to an integer, to be used in if statement.

if age >= 18:                                                                   # beginning of control structure with if, elif & else statements
    print("You are old enough!")                                                # print statement outputs You are old enough if user is at least 18 years old
elif age > 16:
    print("Almost there")                                                       # print statement outputs Almost there for users older than 16 but younger than 18
else:
    print("You are too young")                                                  # print statement outputs You are too young if user is under 16
            
for i in range(age):                                                            # for loop which prints every number from 0 to the user input for age variable
    if i <= age:
        print(i)