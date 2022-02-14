import random
import timeit


class Utility:
    def __init__(self):
        pass

    def generateTestArray(self):
        a = []
        for i in range(1000):
            a.append(random.randint(0, 100))
        return a


def SCAN(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] == a[j]:
                print(i, " - ", j)
                print(a[i])
                return
            else:
                continue


def STOR(a):
    n = len(a)
    b = [0] * 10000
    for i in range(n):
        if b[a[i]] == 1:
            print("meet duplicate when i = ", i)
            print(a[i])
            return
        else:
            b[a[i]] = 1
            continue


util = Utility()

array_a = util.generateTestArray()

print(array_a)
def runScan():
    SCAN(array_a)

def runStor():
    STOR(array_a)

print(timeit.Timer(runScan).timeit(number=100))
print(timeit.Timer(runStor).timeit(number=100))
