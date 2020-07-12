"""
	Regex : Regular Expression Algorithm Module
"""
import re  	# Regular expression module in python
from typing import List

def regex_function(pattern: str, text: str) -> List[int]:
	iter = re.finditer(pattern, text)
	return [m.start(0) for m in iter]