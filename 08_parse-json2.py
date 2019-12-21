# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:20:03 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key = "Oiqs2PQscXg2fG7DDMU9LbEjGr18V50s"

url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URL: " + (url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
    
