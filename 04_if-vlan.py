# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 12:31:24 2019

@author: CEC
"""

nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("This native VLAN and the data VLAN are different.")
