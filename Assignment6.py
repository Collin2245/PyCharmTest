import random
import timeit


def generateTestArray(size, lowEnd, highEnd):
    a = []
    for i in range(size):
        a.append(random.randint(lowEnd, highEnd))
    return a


def selectionSort2(a):
    for i in range(len(a)):
        valAtI = a[i]
        answer = list(findSmallest(makeMiniArray(i, a)))
        smallestVal = int(answer[0])
        index = int(answer[1] + i)
        a[i] = smallestVal;
        a[int(index)] = valAtI
        print(a)
    return a


def selectionSort(a):
    for i in range(len(a)):
        minValPos = i
        for j in range(i + 1, len(a)):
            if a[minValPos] > a[j]:
                minValPos = j
        a[i], a[minValPos] = a[minValPos], a[i]
    return a


def findSmallest(a):
    smallestNum = 999999999
    index = 0;
    answer = []
    for i in range(len(a)):
        if a[i] < smallestNum:
            index = i
            smallestNum = a[i]
    answer.append(smallestNum)
    answer.append(index)

    return answer


def insertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = temp


def makeMiniArray(x, a):
    output = []
    for i in range(x, len(a)):
        output.append(a[i])
    return output


def bubbleSort(a):
    for i in range(len(a)):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


s = generateTestArray(10, 0, 20)
m = generateTestArray(1000, 0, 2000)
l = generateTestArray(100000, 0, 200000)


def bubbleSorts():
    print("bubble sort small")
    bubbleSort(s)


def bubbleSortm():
    print("bubble sort medium")
    bubbleSort(m)


def bubbleSortl():
    print("bubble sort large")
    bubbleSort(l)


def selectionSorts():
    print("selection sort small")
    selectionSort(s)


def selectionSortm():
    print("selection sort medium")
    selectionSort(m)


def selectionSortl():
    print("selection sort large")
    selectionSort(l)

def insertionSorts():
    print("insertion sort small")
    insertionSort(s)

def insertionSortm():
    print("insertion sort medium")
    insertionSort(m)

def insertionSortl():
    print("insertion sort large")
    insertionSort(l)


print("bubble sort s: ", timeit.Timer(bubbleSorts).timeit(number=1))
print("bubble sort m: ", timeit.Timer(bubbleSortm).timeit(number=1))
print("bubble sort l: ", timeit.Timer(bubbleSortl).timeit(number=1))
print("selection sort s: ", timeit.Timer(selectionSorts).timeit(number=1))
print("selection sort m: ", timeit.Timer(selectionSortm).timeit(number=1))
print("selection sort l: ", timeit.Timer(selectionSortl).timeit(number=1))
print("insertion sort s: ", timeit.Timer(insertionSorts).timeit(number=1))
print("insertion sort m: ", timeit.Timer(insertionSortm).timeit(number=1))
print("insertion sort l: ", timeit.Timer(insertionSortl).timeit(number=1))
