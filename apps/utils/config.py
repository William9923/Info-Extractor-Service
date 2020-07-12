import string
import random

def generate_prefix_key():
    return "/api/v1"

def generate_random_seperator():
    return random.choice(['\x0c', '\x0b'])