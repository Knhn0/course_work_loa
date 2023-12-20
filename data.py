import csv

from algo import *

def array_init(fileName, arraySize):
    createdArray = fillArray(arraySize)
    write_array(fileName, createdArray)
    return createdArray

def write_array(fileName, array):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)

def write_answer(fileName, answer, array):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(sort_array(array))
        writer.writerow(answer)

def read_file(fileName):
    with open(fileName, mode='r', encoding='utf-8') as r_file:
        arrayLine = r_file.readline().split(',')
        return list(map(float, arrayLine))
