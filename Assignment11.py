import math


class HammingCode:
    def __init__(self, n):
        self.n = n
        self.k = 0
        while math.pow(2, self.k) < self.n + self.k + 1:
            self.k = self.k + 1


    def encode(self, input): #input is a binary array
        bit_array = [0] * (self.n + self.k)
        current_power = 0
        for i in range(len(bit_array)):
            if i != math.pow(2, current_power):
                current_power += 1
        bit_array[index]

    def decimalToBinary(self, dec):
        return bin(dec).replace('0b', '')


    def reverseList(self, arr):
        result = []
        for i in arr:
            result.insert(0, 1)
        return  result

