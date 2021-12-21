import itertools

d2 = [['th'], ['wats'], ['oahg'], ['fgdt']]
words = ['this' 'two', 'fat', 'fgdt']

def findVertical(x, p):
    found = False
    wordLen = len(x)
    verticalLines = 0
    verticalLines = 0
    foundWordIndexes = []
    """Horizontal check"""
    verticalLists = []
    v = ''
    for i in range(len(p)):
        v = ''
        for lists in p:
            if len(lists[0]) >= i + 1:
                letter = lists[0][i]
                print(letter, ' : -> ')
                v += '%s' % letter
        verticalLists.append([v])
    print(verticalLists)
    print(findHorizontal(x, verticalLists))
    return 0

def displayPuzzle(puzzle):
    print('----------------------------')
    for lists in puzzle:
        for list in lists:
            for word in list:
                print('  ', word, end='  ')
            print()
    print('----------------------------')


def findHorizontal(x, p):
    found = False
    wordLen = len(x)
    horizontalLines = 0
    verticalLines = 0
    foundWordIndexes = []
    """Horizontal check"""
    for lists in p:
        foundWordIndexes = []
        horizontalLines += 1
        for letter in lists[0]:
            if letter == x[0] and not len(lists[0]) < wordLen:
                letterIndex = lists[0].index(letter)
                letterTooLongAfterPrefix = len(lists[0][letterIndex:]) < wordLen
                if not letterTooLongAfterPrefix:
                    listCheck = lists[0][letterIndex:]
                    foundWordIndexes.append(letterIndex)
                    for s in range(1, wordLen):
                        if x[s] == listCheck[s]:
                            letterIndex += 1
                            foundWordIndexes.append(letterIndex)
                    if len(foundWordIndexes) == wordLen:
                        return 'Row %s of indexes : %s' % (horizontalLines, foundWordIndexes)
    return 0


print(findHorizontal('hg', d2))


displayPuzzle(d2)
print()
print()
print()
print(findVertical('ah', d2))

def diagonal(x, p):
    found = False
    wordLen = len(x)
    verticalLines = 0
    verticalLines = 0
    foundWordIndexes = []
    """Horizontal check"""
    for lists in p:
        foundWordIndexes = []
        if len(lists[0]) >= verticalLines:
            letter = lists[0][verticalLines]
            print(letter)
            nextletters = []
            for ls in range(verticalLines, len(p)):
                if len(p[verticalLines][0]) >= verticalLines:
                    le = lists[0][verticalLines]
                    nextletters.append(le)
            if letter == x[0] and not len(nextletters) < wordLen:
                letterIndex = lists[0].index(letter)
                foundWordIndexes.append(letterIndex + 1)
                for s in range(verticalLines, wordLen):
                    if x[s] == nextletters[s]:
                        letterIndex += 1
                        foundWordIndexes.append(letterIndex + 1)
                if len(foundWordIndexes) == wordLen:
                    return 'column %s of indexes : %s' % (verticalLines + 1, foundWordIndexes)
        verticalLines += 1
    return 0
