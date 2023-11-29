import random
from random import randint
from re import fullmatch
from time import time_ns

import np as np

REGEX_PATTERN = r'\d+'
NANOS_IN_MILLIS = 1_000_000
RANDOM_MIN = 0.0
RANDOM_MAX = 100.0

def fillArray(size):
    return [random.uniform(0.0, 100.0) for _ in range(size)]

def sortArray(a):
    n = len(a)
    s, counter = 0.0, 0.0
    for i in range(n - 1):
        s += i
        counter += 1
    percent = s / counter
    if float(81) <= percent <= float(100):
        return "5"
    elif float(61) <= percent <= float(80):
        return "4"
    elif float(41) <= percent <= float(60):
        return "3"
    else:
        return "2"

def isValidInput(user_input):
    return fullmatch(REGEX_PATTERN, user_input)

def measureTime(function, *args):
    start = time_ns()
    function(*args)
    finish = time_ns()
    return (finish - start) // NANOS_IN_MILLIS
