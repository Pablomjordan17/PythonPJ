# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 09:36:26 2019

@author: CEC
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "Oiqs2PQscXg2fG7DDMU9LbEjGr18V50s"
    
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destitation: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")