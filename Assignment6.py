
def selectionSort(a):
    for i in range(len(a)):
        valAtI = a[i]
        answer = list(findSmallest(makeMiniArray(i, a)))
        smallestVal = int(answer[0])
        index = int(answer[1]+i)
        a[i] = smallestVal;
        a[int(index)] = valAtI
        print(a)
    return a


def findSmallest(a):
    smallestNum = 999999999
    index = 0;
    answer= []
    for i in range(len(a)):
        if a[i] < smallestNum:
            index = i
            smallestNum = a[i]
    answer.append(smallestNum)
    answer.append(index)

    return answer

def makeMiniArray(x,a):
    output = []
    for i in range(x, len(a)):
        output.append(a[i])
    return output


print(makeMiniArray(1,[0, 1, 2, 3, 4, 5]))
ar = [3,2,1,0,9,4325,23,0,0,4,503,5,3]
print("len: ",len(ar))
print(selectionSort(ar))