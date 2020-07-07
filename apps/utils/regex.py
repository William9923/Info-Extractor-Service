"""
	Regex : Regular Expression Algorithm Module
"""
import re  	# Regular expression module in python

def regex_function(pattern, text):
	iter = re.finditer(pattern, text)
	return [m.start(0) for m in iter]