list = {
    "A": 0.25,
    "B":0.21,
    "C":0.18,
    "D":0.16
}


class Node:
    def __init__(self, symbol, value, left=None, right=None):
        self.symbol = symbol
        self.value = value
        self.left = left
        self.right = right
        self.huff = ''

    def isLeft(self):
        return self.left is None and self.right is None

    def updateHuff(self):
        if not self.isLeaf():
            self.left.huff = self.huff + '0'
            self.left.updateHuff()
            self.right.huff = self.huff + '1'
            self.right.updateHuff()

    def printHuff(self):
        if not self.isLeaf():
            self.left.printHuff()
            self.right.printHuff()
        else:
            print(f'{self.symbol} -- {self.value} -- {self.huff}')

class HuffmanTree:
    def __init__(self):
        self.root = None

    def BuildTree(self, input):
        leafArray = []
        for key in input:
            leafNode = Node(key, input[key])
            leafArray.append(leafNode)

        leafArray.sort(key = lambda x: x.value, reverse=True)
        while len(leafArray) > 1:
            right = leafArray.pop()
            left = leafArray.pop()
            parentNode = Node(left.symbol + right.symbol, left.value + right.value, left, right)
            leafArray.append(parentNode)

        self.root = leafArray[0]

    def updateHuff(self):
        self.root.updateHuff()

    def printHuff(self):
        self.root.printHuff()



tree = HuffmanTree()
tree.buildTree(list)
tree.updateHuff()
tree.printHuff()

