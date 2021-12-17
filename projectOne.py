"""
parentIndex = (index - 1) // 2
leftChildIndex = 2 * index + 1
rightChildIndex = 2 * index + 2
"""
import math
import timeit
from io import StringIO


class Node:
    def __init__(self, data):
        self.data = data
        self.frequency = 1


class binaryHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    """Helper methods"""

    def getParentIndex(self, index):
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def hasParent(self, index):
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def parentData(self, index):
        """Get parent data"""
        return self.storage[self.getParentIndex(index)]

    def leftChildData(self, index):
        """Get left child data"""
        return self.storage[self.getLeftChildIndex(index)]

    def rightChildData(self, index):
        """Get right child data"""
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        """Does the swapping while going up or down"""
        item1 = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = item1

    """Main operations"""

    def insert(self, data):
        if self.isFull():
            print("Heap is full buddy! unable to add " + str(data))
            return
        elif data in self.storage[:self.size - 1]:
            return
        else:
            self.storage[self.size] = data
            self.size += 1
            self.heapifyUp(self.size - 1)

    def heapifyUp(self, currentIndex):
        if self.hasParent(currentIndex) and self.parentData(currentIndex) > self.storage[currentIndex]:
            self.swap(self.getParentIndex(currentIndex), currentIndex)
            self.heapifyUp(self.getParentIndex(currentIndex))

    def removeMin(self):
        if self.size <= 0:
            print('Heap is empty buddy')
            pass
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size - 1]
            self.size -= 1
            self.heapifyDown(0)
            return data

    def heapifyDown(self, index):
        smallestIndex = index
        if self.hasLeftChild(index) and self.storage[smallestIndex] > self.leftChildData(index):
            smallestIndex = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.storage[smallestIndex] > self.rightChildData(index):
            smallestIndex = self.getRightChildIndex(index)
        if smallestIndex != index:
            self.swap(index, smallestIndex)
            self.heapifyDown(smallestIndex)

    def preOrder(self, index, orderList):
        if index == self.size:
            return
        orderList.append(self.storage[index])
        if self.hasLeftChild(index):
            self.preOrder(self.getLeftChildIndex(index), orderList)
        if self.hasRightChild(index):
            self.preOrder(self.getRightChildIndex(index), orderList)
        return orderList

    def inOrder(self, index, orderList):
        if index == self.size:
            return
        if self.hasLeftChild(index):
            self.inOrder(self.getLeftChildIndex(index), orderList)
        orderList.append(self.storage[index])
        if self.hasRightChild(index):
            self.inOrder(self.getRightChildIndex(index), orderList)
        return orderList

    def postOrder(self, index, orderList):
        if index == self.size:
            return
        if self.hasLeftChild(index):
            self.postOrder(self.getLeftChildIndex(index), orderList)
        if self.hasRightChild(index):
            self.postOrder(self.getRightChildIndex(index), orderList)
        orderList.append(self.storage[index])
        return orderList

    def show_tree(self, total_width=50, fill=' '):
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.storage):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)


class buildHeap:
    def __init__(self, arr):
        self.size = len(arr)
        self.storage = arr
        self.build()

    def build(self):
        startIdx = self.size // 2 - 1
        for elements in range(startIdx, -1, -1):
            self.heapifyDown(elements)

    def heapifyDown(self, index):
        smallestIndex = index
        if self.hasLeftChild(index) and self.storage[smallestIndex] > self.leftChildData(index):
            smallestIndex = self.getLeftChildIndex(index)
        if self.hasRightChild(index) and self.storage[smallestIndex] > self.rightChildData(index):
            smallestIndex = self.getRightChildIndex(index)
        if smallestIndex != index:
            self.swap(index, smallestIndex)
            self.heapifyDown(smallestIndex)

    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size

    def leftChildData(self, index):
        """Get left child data"""
        return self.storage[self.getLeftChildIndex(index)]

    def rightChildData(self, index):
        """Get right child data"""
        return self.storage[self.getRightChildIndex(index)]

    def getLeftChildIndex(self, index):
        return 2 * index + 1

    def getRightChildIndex(self, index):
        return 2 * index + 2

    def swap(self, index1, index2):
        """Does the swapping while going up or down"""
        item1 = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = item1

    def removeMin(self):
        if self.size <= 0:
            print('Heap is empty buddy')
            pass
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size - 1]
            self.size -= 1
            self.heapifyDown(0)
            return data

    def preOrder(self, index, orderList):
        if index == self.size:
            return
        orderList.append(self.storage[index])
        if self.hasLeftChild(index):
            self.preOrder(self.getLeftChildIndex(index), orderList)
        if self.hasRightChild(index):
            self.preOrder(self.getRightChildIndex(index), orderList)
        return orderList

    def inOrder(self, index, orderList):
        if index == self.size:
            return
        if self.hasLeftChild(index):
            self.inOrder(self.getLeftChildIndex(index), orderList)
        orderList.append(self.storage[index])
        if self.hasRightChild(index):
            self.inOrder(self.getRightChildIndex(index), orderList)
        return orderList

    def postOrder(self, index, orderList):
        if index == self.size:
            return
        if self.hasLeftChild(index):
            self.postOrder(self.getLeftChildIndex(index), orderList)
        if self.hasRightChild(index):
            self.postOrder(self.getRightChildIndex(index), orderList)
        orderList.append(self.storage[index])
        return orderList

    def show_tree(self, total_width=50, fill=' '):
        """Pretty-print a tree.
        total_width depends on your input size"""
        output = StringIO()
        last_row = -1
        for i, n in enumerate(self.storage):
            if i:
                row = int(math.floor(math.log(i + 1, 2)))
            else:
                row = 0
            if row != last_row:
                output.write('\n')
            columns = 2 ** row
            col_width = int(math.floor((total_width * 1.0) / columns))
            output.write(str(n).center(col_width, fill))
            last_row = row
        print(output.getvalue())
        print('-' * total_width)


def presentingAlgorithms():
    # --------------------------------------------------------------------------------------------
    """Given inputs"""
    inputs = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]
    # --------------------------------------------------------------------------------------------
    print('\n\n')
    print("""Using successive insertion O(n*LogN)""")
    heap = binaryHeap(len(inputs))
    for i in inputs:  # insertion loop
        heap.insert(i)
    heap.show_tree()
    print('Level Order:           ', heap.storage)
    print('In Order Traversing:   ', heap.inOrder(0, []))
    print('Pre Order Traversing:  ', heap.preOrder(0, []))
    print('Post Order Traversing: ', heap.postOrder(0, []))
    print('\n')
    print('*************' * 10)
    # --------------------------------------------------------------------------------------------
    print('\n')
    print("""Using linear algorithm O(n)""")
    built = buildHeap(inputs)
    built.show_tree()
    print('Level Order:           ', built.storage)
    print('In Order Traversing:   ', built.inOrder(0, []))
    print('Pre Order Traversing:  ', built.preOrder(0, []))
    print('Post Order Traversing: ', built.postOrder(0, []))
    print('*************' * 10)
    # --------------------------------------------------------------------------------------------


def successiveHeap(N):
    heap = binaryHeap(len(N))
    for i in N:  # insertion loop
        heap.insert(i)


def buildHeapMethod(N):
    built = buildHeap(N)


presentingAlgorithms()
