import csv

from algo import *

def arrayInit(fileName, arraySize):
    createdArray = fillArray(arraySize)
    writeArray(fileName, createdArray)
    return createdArray

def writeArray(fileName, array):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)

def writeAnswer(fileName, answer, array):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)
        writer.writerow(answer)

def readFile(fileName):
    with open(fileName, mode='r', encoding='utf-8') as r_file:
        arrayLine = r_file.readline().split(',')
        return list(map(float, arrayLine))
