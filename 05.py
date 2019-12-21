# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:11:06 2019

@author: CEC
"""

aclNum = int(input("What is the IPv4 ACL number? "))
if aclNum >= 1 and aclNum <= 99:
    print("This is a standard IPv4 ACL.")
elif aclNum >=100 and aclNum <=199:
    print("This is a extended IPv4 ACL.")
else:
    print("This is not a standard or extended IPv4 ACL.")