# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 09:36:25 2019

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

    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    y = testData[i]
    print(y,"-> ",end=" ")
    result = isYearLeap(y)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
        
def daysInMonth(y, m):
    if y < 1 or m < 1 or m > 12:
        return None
    elif m == 2:
        return 28
    elif m == 1:
        return 31
    elif m == 3:
        return 31
    elif m == 4:
        return 30
    elif m == 5:
        return 31
    elif m == 6:
        return 30
    elif m == 7:
        return 31
    elif m == 8:
        return 31
    elif m == 9:
        return 30
    elif m == 10:
        return 31
    elif m == 11:
        return 30
    elif m == 12:
        return 31
    elif isYearLeap(y) and m == 2:
        return 29
    

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