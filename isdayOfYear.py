# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:09:41 2019

@author: CEC
"""

def isYearLeap(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True

        
def daysInMonth(y, m):
    if y < 1 or m < 1 or m > 12:
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res = days[m - 1]
    if m == 2 and  isYearLeap(y):
        res = 29
    return res

        
def dayOfYear(year, month, day):
    months = [2,4,6,9,11]
    if year < 1500 or month <1 or month > 12 or day <1 or day > 31:
        return None
    elif not isYearLeap(year) and month == 2 and day > 28:
        return None
    elif month in months and day > 30 :
        return None
    days = 0
    for i in range (1,12+1):
        days += daysInMonth(year,i)
    
    return days
   
print(dayOfYear(2020, 12, 31))
    