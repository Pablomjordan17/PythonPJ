# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 08:41:48 2019

@author: CEC
"""

def isPrime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" " )
print()
        