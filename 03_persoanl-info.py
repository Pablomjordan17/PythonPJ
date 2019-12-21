# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:13:27 2019

@author: CEC
"""

while True:
    firstName =input("Whats your first name? ")
    lastName = input("Whats your last name? ")
    location = input("Where are you front? ")
    age = int(input("How old are you? "))
    x=int(age)

    space=" "
    print("Hi" + space + "my" + space + "name" + space + "is" + space + firstName + space + lastName)
    if age >=0 and age <=25:
        print("You are very young")
    elif age >=26 and age <=40:
        print("You are young")
    else:
        print("You are no longer young")
    
    quit=input("Do you want to exit? [Y] or [N]")
    if quit == 'Y':
        break


