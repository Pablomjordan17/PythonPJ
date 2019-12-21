# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:05:33 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "Oiqs2PQscXg2fG7DDMU9LbEjGr18V50s"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)