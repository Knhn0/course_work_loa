import csv

from algo import *

def arrayInit(fileName, arraySize):
    createdArray = fillArray(arraySize)
    writeFile(fileName, createdArray)
    return createdArray

def writeFile(fileName, array):
    with open(fileName, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(array)
def readFile(fileName):
    with open(fileName, mode='r', encoding='utf-8') as r_file:
        arrayLine = r_file.readline().split(',')
        return list(map(float, arrayLine))
