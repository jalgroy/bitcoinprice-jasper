#!/usr/bin/env python2
import requests
import random
import re

WORDS = ['bitcoin']

def isValid(text):
	return bool(re.search(r'\bbitcoin\b', text, re.IGNORECASE))

def handle(text, mic, profile):
	
	r =requests.get('https://winkdex.com/api/v0/price')
	response = r.json()

	price = response["price"]
	price = round(price / 100.00, 2)
	
	messages = ["One bitcoin is currently worth %s U.S. Dollars" % price,
			"The price of one bitcoin is %s U.S. Dollars" % price]
	message = random.choice(messages)

	mic.say(message)


