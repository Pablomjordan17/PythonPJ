# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:04:49 2019

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

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	y = testYears[i]
	m = testMonths[i]
	print(y, m, "->", end="")
	result = daysInMonth(y, m)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")

        