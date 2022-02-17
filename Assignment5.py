import random
import timeit
import sys
import numpy as np
from bitarray import bitarray

class Utility:
    def __init__(self):
        pass

    def generateTestArray(self):
        a = []
        for i in range(1000):
            a.append(random.randint(0, 100))
        return a

    def generateTestArray2(self, size):
        a = []
        randNum = random.randint(0 , size - 1)
        a.append(randNum)
        for i in range(size -1):
            a.append(i)
        shuffledArray = util.shuffle(a)
        return shuffledArray

    def shuffle(self, a):
        timesToShuffle = random.randint(1,9)
        startPoint = random.randint(0,len(a));
        firstHalf = a[startPoint:]
        secondHalf = a[:startPoint]
        for i in range(timesToShuffle):
            output = []
            while(firstHalf or secondHalf):
                if firstHalf:
                    temp = random.randint(0, 1)
                    if(temp == 1):
                        output.append(firstHalf[0])
                        del firstHalf[0]
                if secondHalf:
                    temp = random.randint(0,1)
                    if(temp ==1 ):
                        output.append(secondHalf[0])
                        del secondHalf[0]
            startPoint = random.randint(0, len(a));
            firstHalf = output[startPoint:]
            secondHalf = output[:startPoint]
            print(startPoint)

        print("output: ", output)
        print(len(output))
        return output






def SCAN(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                print("duplicate scan 1: " ,a[i])
                return
            else:
                continue

def SCAN2(a):
    for i in range(len(a)-1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                print("duplicate scan 2: ", a[i])
                return a[i]
            else:
                continue

@profile
def STOR(a):
    n = len(a) + 99
    b = [0] * (len(a) + 99)
    for i in range(n):
        if b[a[i]] == 1:
            print("duplpicate stor 1: ", a[i])
            return
        else:
            b[a[i]] = 1
            continue


# def STOR2(a):
#
#     b = bytearray(len(a) + 99)
#     for i in range(len(a)):
#         if b[a[i]] == 1:
#             print("duplpicate stor 2: ", a[i])
#             return
#         else:
#             b[a[i]] = 1
#             continue

@profile
def STOR2(a):

    b = bitarray(len(a) + 99)
    b.setall(0)
    #print("b ",b)
    for i in range(len(a)):
        if b[a[i]] == 1:
            print("duplpicate stor 2: ", a[i])
            print(b)
            return
        else:
            b[a[i]] = 1
            continue

util = Utility()

array_a = util.generateTestArray()
array_b = util.generateTestArray2(500000)

#print(array_a)
def runScan():
    SCAN(array_b)

def runStor():
    STOR(array_b)

def runScan2():
    SCAN2(array_b)

def runStor2():
    STOR2(array_b)

#print("stor 1: ", sys.getsizeof([0] * 100))
#print("stor 2: ", sys.getsizeof(bytearray(100)))
#a = bytearray(100)
#a[0] = 1
#print(bytearray(100))
#print(a[0])
print("scan 1: ", timeit.Timer(runScan).timeit(number=1))
print("stor 1: ", timeit.Timer(runStor).timeit(number=1))
print("scan 2: ", timeit.Timer(runScan2).timeit(number=1))
print("stor 2: ", timeit.Timer(runStor2).timeit(number=1))
