import sys
from io import StringIO
import math


class Node_bst:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Node_rbt:
    def __init__(self, data):
        self.data = data  # holds the key
        self.parent = None  # pointer to the parent
        self.left = None  # pointer to left child
        self.right = None  # pointer to right child
        self.color = 1  # 1 . Red, 0 . Black


class Node_avl(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1


class bsTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, key):
        if self.size == 0:
            self.root = Node_bst(key)
        self.insertNode(self.root, key)
        self.size += 1

    def insertNode(self, root, key):
        if root is None:
            return Node_bst(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insertNode(root.right, key)
            else:
                root.left = self.insertNode(root.left, key)
        return root

    def inorder(self):
        self.in_order(self.root)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.val)
            self.in_order(root.right)


class rbTree:
    def __init__(self):
        self.TNULL = Node_rbt(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, key):
        # Ordinary Binary Search Insertion
        node = Node_rbt(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1  # new node must be red

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        # y is parent of x
        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        # if new node is a root node, simply return
        if node.parent is None:
            node.color = 0
            return

        # if the grandparent is None, simply return
        if node.parent.parent is None:
            return

        # Fix the tree
        self.__fix_insert(node)

    def __fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left  # uncle
                if u.color == 1:
                    # case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        # case 3.2.2
                        k = k.parent
                        self.right_rotate(k)
                    # case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right  # uncle

                if u.color == 1:
                    # mirror case 3.1
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        # mirror case 3.2.2
                        k = k.parent
                        self.left_rotate(k)
                    # mirror case 3.2.1
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def __in_order_helper(self, node):
        if node != self.TNULL:
            self.__in_order_helper(node.left)
            sys.stdout.write(str(node.data) + " ")
            self.__in_order_helper(node.right)

    def inorder(self):
        self.__in_order_helper(self.root)


class AVLTree(object):
    x = None

    def insert(self, root_in, key):

        if not root_in:
            return Node_avl(key)
        elif key < root_in.value:
            root_in.l = self.insert(root_in.l, key)
        else:
            root_in.r = self.insert(root_in.r, key)

        root_in.h = 1 + max(self.getHeight(root_in.l),
                            self.getHeight(root_in.r))

        b = self.getBal(root_in)

        if b > 1 and key < root_in.l.value:
            return self.rRotate(root_in)

        if b < -1 and key > root_in.r.value:
            return self.lRotate(root_in)

        if b > 1 and key > root_in.l.value:
            root_in.l = self.lRotate(root_in.l)
            return self.rRotate(root_in)

        if b < -1 and key < root_in.r.value:
            root_in.r = self.rRotate(root_in.r)
            return self.lRotate(root_in)
        self.x = root_in
        return root_in

    def lRotate(self, z):
        y = z.r
        T2 = y.l
        y.l = z
        z.r = T2
        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))
        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                      self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                      self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.h

    def getBal(self, root):
        if not root:
            return 0
        return self.getHeight(root.l) - self.getHeight(root.r)

    def inOrder(self):
        self.in_order(self.x)

    def in_order(self, root):
        if not root:
            return
        self.in_order(root.l)
        print("{0} ".format(root.value), end="")
        self.in_order(root.r)


def successiveInsertionBST(N):
    newTree = bsTree()
    for i in N:
        newTree.insert(i)
    return newTree


def successiveInsertionRBT(N):
    newTree = rbTree()
    for i in N:
        newTree.insert(i)
    return newTree


def successiveInsertionAVL(N):
    newTree = AVLTree()
    root = None
    for i in N:
        root = newTree.insert(root, i)
    return newTree


numbersFiles = "numbers.txt"


def menu(input_number):
    my_list = []
    with open(numbersFiles, 'r') as numbers:
        for x in range(input_number):
            my_list.append(int(numbers.readline().strip('\n')))
    return my_list


def testObjects():
    bst = bsTree()

    bst.insert(1)
    bst.insert(13)
    bst.insert(4)
    bst.insert(2)
    bst.inorder()

    rbt = rbTree()
    rbt.insert(8)
    rbt.insert(18)
    rbt.insert(5)
    rbt.insert(15)
    rbt.insert(17)
    rbt.insert(25)
    rbt.insert(40)
    rbt.insert(80)
    rbt.inorder()
    print()
    print('-' * 100)
    Tree = AVLTree()

    root = Tree.insert(None, 1)
    root = Tree.insert(root, 2)
    root = Tree.insert(root, 3)
    root = Tree.insert(root, 4)
    root = Tree.insert(root, 5)
    root = Tree.insert(root, 6)

    # Preorder Traversal
    print("AVL tree: ")
    Tree.inOrder()
    print()

    inputs = menu(100)
    a = successiveInsertionAVL(inputs)
    b = successiveInsertionBST(inputs)
    r = successiveInsertionRBT(inputs)
