class HashTable1:
    M = 31

    def __init__(self):
        self.array = [[]] * self.M

    def Hash(self, key):
        temp = 0
        for char in key:
            temp += ord(char)
        return temp % self.M

    def insert(self, key, value):
        hashcode = self.Hash(key)
        found = len(self.array[hashcode]) > 0
        if found is True:
            for i in range(self.array[hashcode]):
                if self.array[hashcode][i]["key"] == key:
                    self.array[hashcode][i]["index"].append(value["index"][0])
                    return hashcode
            self.array[hashcode].append(value)
            return hashcode
        else:
            self.array[hashcode].append(value)

    def search(self, key):
        hashcode = self.Hash(key)
        if len(self.array[hashcode]) > 0:
            for i in range(len(self.array[hashcode])):
                if self.array[hashcode][i]["key"] == key:
                    return self.array[hashcode][i]["index"]
            return None
        else:
            return None


class HashTable2:
    M = 31
    g = 5**(1/2)

    def __init__(self):
        self.array = [ None ] * self.M

    def IsFull(self):
        self.count == self.M

    def Hash(self, key):
        temp = 0
        for char in key:
            temp += ord(char)
        a = temp * self.g
        f = a - int(a)
        return int(f * self.M)

    def insert(self, key, value):
        hashcode = self.Hash(key)
        if self.IsFull():
            return None
        else:
            if self.array[hashcode] is None:
                self.array[hashcode] = value
            else:
                counter = 0
                while self.array[hashcode + counter] is not None:
                    if hashcode + counter == self.M:
                        counter = 0 - hashcode
                    else:
                        counter += 1
                self.array[hashcode + counter] = value

    def search(self, key):
        hashcode = self.Hash(key)
        if len(self.array[hashcode]) > 0:
            for i in range(len(self.array[hashcode])):
                if self.array[hashcode][i] == key:
                    return self.array[hashcode][i]
            return None
        else:
            return None



def RemovePunctuation(poem):
    punctuationList = [",", ".", ";", "!", ":"]
    newString = ""
    for char in poem:
        if char not in punctuationList:
            newString += char
    return newString

def ConvertToList(poem):
    return poem.split()

string = "COME away, come away, death, And in sad cypres let me be laid; Fly away, fly away, breath; I am slain by a fair cruel maid. My shroud of white, stuck all with yew, O prepare it! My part of death, no one so true Did share it. Not a flower, not a flower sweet, On my black coffin let there be strown; Not a friend, not a friend greet My poor corse, where my bones shall be thrown: A thousand thousand sighs to save, Lay me, O, where Sad true lover never find my grave To weep there!"
inputString = ConvertToList(RemovePunctuation(string))
print(inputString)

ht1 = HashTable1()
ht2 = HashTable2()

for i in inputString:
    print(ht1.array)
    ht1.array.insert(i,i)

for i in inputString:
    print(ht2.array)
    ht2.insert(i,i)


