import math

inputs = [4371, 1323, 6173, 4199, 4344, 9679, 1989, 9000, 8000, 90, 700, 45, 69, 79, 32, 15, 46, 963]

""" a) Separate chaining hash table. """


def isPrime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n) + 1), 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def nextPrime(Number):
    if Number <= 1:
        return 2

    prime = Number
    found = False

    while not found:
        prime = prime + 1

        if isPrime(prime) is True:
            found = True

    return prime


class separate_chaining:
    def __init__(self):
        self.HashTable = [[] for x in range(10)]

    def display_hash(self):
        for i in range(len(self.HashTable)):
            print(i, end=", ")

            for j in self.HashTable[i]:
                print("-->", end=" ")
                print(f'{j:<5}', end=" ")
            print()

    def Hashing(self, keyValue):
        return keyValue % len(self.HashTable)

    def insert(self, keyValue):
        hash_key = self.Hashing(keyValue)
        self.HashTable[hash_key].append(keyValue)


class linearHash:
    def __init__(self, N):
        self.HashTable = [None] * N
        self.capacity = N
        self.size = 0
        self.reloadFactor = 0.4
        self.x = 0

    def Hashing(self, keyValue):
        return keyValue % self.capacity

    def insert(self, keyValue):
        index = self.Hashing(keyValue)

        while self.HashTable[index] is not None:
            self.x += 1
            index = (self.Hashing(keyValue) + self.x) % self.capacity
        k = keyValue if self.HashTable[index] is None else self.HashTable[index]  # technique to replace none by int
        self.HashTable[index] = k
        self.size += 1
        self.x = 0
        if (self.size / self.capacity) >= self.reloadFactor:
            self.reHash()

    def reHash(self):
        self.size = 0
        oldValues = self.HashTable
        self.capacity = nextPrime(2 * self.capacity)
        self.HashTable = [None] * self.capacity
        for i in oldValues:
            if i is not None:
                self.insert(i)

    def display_hash(self):
        for i in range(len(self.HashTable)):
            if self.HashTable[i] is None:
                print(i, "-->", " ")
            else:
                print(i, "-->", f'{self.HashTable[i]:<5}')


class quadraticHash:
    def __init__(self, N):
        self.HashTable = [None] * N
        self.capacity = N
        self.size = 0
        self.reloadFactor = 0.4
        self.x = 0

    def Hashing(self, keyValue):
        return keyValue % len(self.HashTable)

    def insert(self, keyValue):
        index = self.Hashing(keyValue)

        while self.HashTable[index] is not None:
            self.x += 1
            p = self.x ** 2 % self.capacity
            index = (self.Hashing(keyValue) + p) % self.capacity
        k = keyValue if self.HashTable[index] is None else self.HashTable[index]  # technique to replace none by int
        self.HashTable[index] = k
        self.size += 1
        self.x = 0
        if (self.size / self.capacity) >= self.reloadFactor:
            self.reHash()

    def display_hash(self):
        for i in range(len(self.HashTable)):
            if self.HashTable[i] is None:
                print(i, ", -->", " ")
            else:
                print(i, ", -->", f'{self.HashTable[i]:<5}')

    def reHash(self):
        self.size = 0
        oldValues = self.HashTable
        self.capacity = nextPrime(2 * self.capacity)
        self.HashTable = [None] * self.capacity
        for i in oldValues:
            if i is not None:
                self.insert(i)


class doubleFunctionHash:
    def __init__(self, N):
        self.HashTable = [None] * N
        self.capacity = N
        self.size = 0
        self.reloadFactor = 0.4
        self.x = 0

    def Hashing(self, keyValue):
        return keyValue % len(self.HashTable)

    def Hashing2(self, keyValue):
        value = 7 - (keyValue % 7)
        if value == 0:
            return 1
        return value

    def insert(self, keyValue):
        index = self.Hashing(keyValue, self.x)

        while self.HashTable[index] is not None:
            self.x += 1
            p = (self.Hashing2(keyValue) % self.capacity)
            index = self.Hashing(keyValue, p)
        k = keyValue if self.HashTable[index] is None else self.HashTable[index]  # technique to replace none by int
        self.HashTable[index] = k
        self.size += 1
        self.x = 0
        if (self.size / self.capacity) >= self.reloadFactor:
            self.reHash()

    def display_hash(self):
        for i in range(len(self.HashTable)):
            if self.HashTable[i] is None:
                print(i, ", -->", " ")
            else:
                print(i, ", -->", f'{self.HashTable[i]:<5}')

    def reHash(self):
        self.size = 0
        oldValues = self.HashTable
        self.capacity = nextPrime(2 * self.capacity)
        self.HashTable = [None] * self.capacity
        for i in oldValues:
            if i is not None:
                self.insert(i)


def testObjects():
    print('---------------------------> separate chaining')
    # hashh = separate_chaining()
    # for i in inputs: hashh.insert(i)
    # hashh.display_hash()
    print('--------------------------->  linear probing')
    v = linearHash(10)
    for i in inputs: v.insert(i)
    v.display_hash()
    print('size: ', v.capacity)
    print('--------------------------->  quadratic probing')
    q = quadraticHash(10)
    for i in inputs: q.insert(i)
    q.display_hash()
    print('------------------------------------- test end')
    print('size: ', q.capacity)


testObjects()
