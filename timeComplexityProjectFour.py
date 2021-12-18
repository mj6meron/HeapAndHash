from projectOne import binaryHeap, buildHeap
import timeit

setUp = '''
from projectFour import bsTree, rbTree, AVLTree
from projectFour import successiveInsertionAVL, successiveInsertionBST,successiveInsertionRBT
from projectOne import successiveHeap
        '''

cycles = 20

numbersFiles = "numbers.txt"


def menu(input_number):
    my_list = []
    with open(numbersFiles, 'r') as numbers:
        for x in range(input_number):
            my_list.append(int(numbers.readline().strip('\n')))
    return my_list


two = menu(2)
four = menu(4)
eight = menu(8)
sixteen = menu(16)
thirtyTwo = menu(32)
sixtyFour = menu(64)

inputsList = [two, four, eight, sixteen, thirtyTwo, sixtyFour]

print('Average running time of %s cycles' % cycles)

for x in inputsList:
    print('')
    usingList = "successiveHeap(%s)" % x
    runningTime_List = timeit.repeat(stmt=usingList, repeat=cycles,
                                     setup=setUp,
                                     number=1)
    averageHeap = '{:.10f}'.format(sum(runningTime_List) / len(runningTime_List))

    usingList2 = "successiveInsertionAVL(%s)" % x
    runningTime_List2 = timeit.repeat(stmt=usingList2, repeat=cycles,
                                      setup=setUp,
                                      number=1)
    averageAVL = '{:.10f}'.format(sum(runningTime_List2) / len(runningTime_List2))

    usingList3 = "successiveInsertionBST(%s)" % x
    runningTime_List3 = timeit.repeat(stmt=usingList3, repeat=cycles,
                                      setup=setUp,
                                      number=1)
    averageBST = '{:.10f}'.format(sum(runningTime_List3) / len(runningTime_List3))

    usingList4 = "successiveInsertionRBT(%s)" % x
    runningTime_List4 = timeit.repeat(stmt=usingList4, repeat=cycles,
                                      setup=setUp,
                                      number=1)
    averageRBT = '{:.10f}'.format(sum(runningTime_List4) / len(runningTime_List4))

    print('''
                          N = %s
        -----------------------------------------------------------------
        Heap Insertion                 : %s
        AVL tree Insertion             : %s
        Binary search tree Insertion   : %s
        Red Black tree Insertion       : %s
        -----------------------------------------------------------------
        ''' % (len(x), averageHeap, averageAVL, averageBST, averageRBT))
