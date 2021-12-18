import timeit

setUp = '''
from projectOne import successiveHeap, buildHeapMethod
        '''

cycles = 2

numbersFiles = "numbers.txt"


def menu(input_number):
    my_list = []
    with open(numbersFiles, 'r') as numbers:
        for x in range(input_number):
            my_list.append(int(numbers.readline().strip('\n')))
    return my_list


fifteen = [10, 12, 1, 14, 6, 5, 8, 15, 3, 9, 7, 4, 11, 13, 2]
hundred = menu(100)
one_thousand = menu(1000)
ten_thousand = menu(10000)
hundred_thousand = menu(100000)

inputsList = [fifteen, hundred, one_thousand, ten_thousand, hundred_thousand]

print('Average running time of %s cycles' % cycles)
for x in inputsList:
    print('')
    usingList = "successiveHeap(%s)" % x
    runningTime_List = timeit.repeat(stmt=usingList, repeat=cycles,
                                     setup=setUp,
                                     number=1)
    averageListSuccessive = '{:.10f}'.format(sum(runningTime_List) / len(runningTime_List))

    usingList2 = "buildHeapMethod(%s)" % x
    runningTime_ListB = timeit.repeat(stmt=usingList2, repeat=cycles,
                                      setup=setUp,
                                      number=1)
    averageListBuildHeap = '{:.10f}'.format(sum(runningTime_ListB) / len(runningTime_ListB))
    print('''
                      N = %s
    -----------------------------------------------------------------
    Successive insertion algorithm  : %s
    BuildHeap/Linear algorithm      : %s
    -----------------------------------------------------------------
    ''' % (len(x), averageListSuccessive, averageListBuildHeap))
