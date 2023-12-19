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

def sort_array(arr):
    if len(arr) > 1:
        pivot = arr.pop()
        grtr_lst, equal_lst, snlr_lst = [], [pivot], []
        for item in arr:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                snlr_lst.append(item)
        return sort_array(snlr_lst) + equal_lst + sort_array(grtr_lst)
    else:
        return arr

def round_arr(arr):
    array = []
    for i in range(len(arr)):
        array.append(round(arr[i]))
    return array

def get_index(arr):
    array = sort_array(round_arr(arr))
    n = len(array)
    s, counter_five, counter_four, counter = 0.0, 0, 0, 0
    for i in range(n - 1):
        if array[i] >= 81:
            counter_five += 1
        elif 61 <= array[i] <= 80:
            counter_four += 1
        counter += 1

    academic_index = (counter_four + counter_five) / counter * 100
    if float(81) <= round(academic_index) <= float(100):
        return "5"
    elif float(61) <= round(academic_index) <= float(80):
        return "4"
    elif float(41) <= round(academic_index) <= float(60):
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
