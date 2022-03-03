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


def GetParentPosition(position):    #get the parent position from child position
    return position // 2


class MinHeap:
    array = []
    count = 0
    def __init__(self):
        self.array.append({
            "value": 0,
            "index": 0,
            "connect": 0
        })

    def HeapPush(self, value, index, connect):  #add a new node to the tree
        self.array.append({
            "value": value,
            "index": index,
            "connect": connect
        })
        self.count += 1
        self.HeapifyUp(self.Size())

    def ExtrudeMin(self):   #take out the root and rebalance the tree
        returnNode = self.GetNode(1)
        lastNode = self.array.pop()
        self.count -= 1
        if self.count > 0:
            self.array[1] = lastNode
        self.HeapifyDown(1)
        return returnNode

    def HeapifyUp(self, position):  #balance the Heap Tree from low to high
        if position <= 1:
            return

        parentPosition = GetParentPosition(position)
        parentNode = self.GetNode(parentPosition)

        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)

        node = 0 #node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2
        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]

        if node != 0:
            self.HeapifyUp(parentPosition)


    def HeapifyDown(self, position):    #balance the tree from high to low
        parentPosition = position
        parentNode = self.GetNode(parentPosition)

        leftPosition = parentPosition * 2
        leftNode = self.GetNode(leftPosition)
        rightPosition = parentPosition * 2 + 1
        rightNode = self.GetNode(rightPosition)

        node = 0  # node = 1, means the leftNode is the smallest, and node = 2 means the rightNode is the smallest
        if leftNode is not None and leftNode["value"] < parentNode["value"]:
            node = 1
        if rightNode is not None and ((node == 1 and rightNode["value"] < leftNode["value"]) or (
                node == 0 and rightNode["value"] < parentNode["value"])):
            node = 2

        if node == 1:
            self.array[leftPosition], self.array[parentPosition] = self.array[parentPosition], self.array[leftPosition]
            self.HeapifyDown(leftPosition)
        elif node == 2:
            self.array[rightPosition], self.array[parentPosition] = self.array[parentPosition], self.array[rightPosition]
            self.HeapifyDown(rightPosition)

    def DecreaseValue(self, value, index, connect): #update the value of the node, since it is decreasing the value, only need heapifyup
        pass

    def Size(self):
        return self.count

    def GetNode(self, position):    #when position is not out of array range, return node. Otherwise return None
        if position > self.count:
            return None #python has None as not exist
        else:
            return self.array[position]

def HeapSort(array):
    heap = MinHeap()
    for i in array:
        heap.HeapPush(i, i, i)
    counter = 0
    while heap.Size() > 0:
        array[counter] = heap.ExtrudeMin()["value"]
        counter += 1
    return array

def MergeSort(array):
    if len(array) > 1:
        midPoint = len(array) // 2

        L = array[:midPoint]
        R = array[midPoint:]

        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1
    return



s = generateTestArray(10, 0, 20)
m = generateTestArray(1000, 0, 2000)
l = generateTestArray(10000, 0, 20000)
big = generateTestArray(100000, 0, 200000)


def heapSorts():
    HeapSort(s)

def heapSortm():
    HeapSort(m)

def heapSortl():
    HeapSort(l)

def heapSortBig():
    HeapSort(big)

def bubbleSorts():
    bubbleSort(s)


def bubbleSortm():
    bubbleSort(m)


def bubbleSortl():
    bubbleSort(l)

def bubbleSortl():
    bubbleSort(l)


def selectionSorts():
    selectionSort(s)


def selectionSortm():
    selectionSort(m)


def selectionSortl():
    selectionSort(l)

def insertionSorts():
    insertionSort(s)

def insertionSortm():
    insertionSort(m)

def insertionSortl():
    insertionSort(l)

def MergeSorts():
    MergeSort(s)

def MergeSortm():
    MergeSort(m)

def MergeSortl():
    MergeSort(l)




print("bubble sort s: ", timeit.Timer(bubbleSorts).timeit(number=1))
print("bubble sort m: ", timeit.Timer(bubbleSortm).timeit(number=1))
print("bubble sort l: ", timeit.Timer(bubbleSortl).timeit(number=1))
print("selection sort s: ", timeit.Timer(selectionSorts).timeit(number=1))
print("selection sort m: ", timeit.Timer(selectionSortm).timeit(number=1))
print("selection sort l: ", timeit.Timer(selectionSortl).timeit(number=1))
print("insertion sort s: ", timeit.Timer(insertionSorts).timeit(number=1))
print("insertion sort m: ", timeit.Timer(insertionSortm).timeit(number=1))
print("insertion sort l: ", timeit.Timer(insertionSortl).timeit(number=1))
print("heap sort s: ", timeit.Timer(heapSorts).timeit(number=1))
print("heap sort m: ", timeit.Timer(heapSortm).timeit(number=1))
print("heap sort l: ", timeit.Timer(heapSortl).timeit(number=1))
#print("heap sort 100,000: ", timeit.Timer(heapSortBig).timeit(number=1))
print("merge sort s: ", timeit.Timer(MergeSorts).timeit(number=1))
print("merge sort m: ", timeit.Timer(MergeSortm).timeit(number=1))
print("merge sort l: ", timeit.Timer(MergeSortl).timeit(number=1))
