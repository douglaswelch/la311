#!/usr/bin/env python

import urllib
import simplejson
from os import system
import os
import time 

# Setup Information

# Data.LaCity.Org URL
api_url = 'https://data.lacity.org/resource/ndkd-k878.json?$where=zipcode=%2291411%22'

# Get JSON data from Google Maps API
response = urllib.urlopen(api_url)
data = simplejson.load(response)   
# print (data)

system("/usr/bin/clear")

# Get 311 Call Data and print last 10 entries
for i in range(0,20):

	c_date = (data[i]['createddate'])
	req = (data[i]['requesttype'])
	addr = (data[i]['address'])
	status = (data[i]['status'])
	
	print status + " " + c_date
	print req
	print "     "+ addr
	print "\n"
	
	


	
	
	