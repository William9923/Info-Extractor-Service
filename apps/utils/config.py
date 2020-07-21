import string
import random

from apps.utils.model.algorithm import *

def generate_prefix_key():
    return "/api/v1"

def generate_random_seperator():
    return random.choice(['\x0c', '\x0b'])
