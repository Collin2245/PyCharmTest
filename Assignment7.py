import random
import timeit


class Node:
    right = None
    left = None
    value = 0

    def __init__(self, value):
        self.value = value


class BinarySearchTree:
    root = None

    def __init__(self):
        pass

    def insertion(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.addNode(self.root, value)

    def addNode(self, root, value):
        if value > root.value:
            if root.right is not None:
                self.addNode(root.right, value)
            else:
                root.right = Node(value)
        elif value < root.value:
            if root.left is not None:
                self.addNode(root.left, value)
            else:
                root.left = Node(value)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self.checkNode(self.root, value)

    def checkNode(self, root, value):
        if root.value > value:
            return self.checkNode(root.left, value)
        elif root.value < value:
            return self.checkNode(root.right, value)
        else:
            return value

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value)
            self.inorder(root.right)


def generateComplexRandomArray():
    arr = []
    for i in range(100000):
        ran = random.randint(0, 999999999)
        arr.append(ran)
    return arr


def generateRandomArray():
    arr = []
    for i in range(5):
        ran = random.randint(0, 50)
        arr.append(ran)
    return arr


def slowSearch(arr, value):
    for i in arr:
        if i == value:
            return value
    return False


tree = BinarySearchTree()
complexBinaryTree = BinarySearchTree()

array = generateRandomArray()
bigArray = generateComplexRandomArray()
print(array)
for a in array:
    tree.insertion(a)
for b in bigArray:
    complexBinaryTree.insertion(b)



tree.inorder(tree.root)
complexBinaryTree.inorder(complexBinaryTree.root)
print("value to search for: ", array[5 - 1])
print("search binary tree: ", tree.search(array[5 - 1]))
print("search slow method: ", slowSearch(array,array[5 - 1]))

print("value to search for big: ", bigArray[100000 - 1])
print("search binary tree big: ", complexBinaryTree.search(bigArray[100000 - 1]))
print("search slow method big: ", slowSearch(bigArray, bigArray[100000 - 1]))


def runBinarySearch():
    complexBinaryTree.search(bigArray[100000 - 1])


def runNormalSearch():
    slowSearch(bigArray, bigArray[100000 - 1])


print("binary search: ", timeit.Timer(runBinarySearch).timeit(number=1))
print("normal search: ", timeit.Timer(runNormalSearch).timeit(number=1))
