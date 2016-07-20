matrix = [['46B', 'E59', 'EA', 'C1F', '45E', '63'],
          ['899', 'FFF', '926', '7AD', 'C4E', 'FFF'],
          ['E2E', '323', '6D2', '976', '83F', 'C96'],
          ['9E9', 'A8B', '9C1', '461', 'F74', 'D05'],
          ['EDD', 'E94', '5F4', 'D1D', 'D03', 'DE3'],
          ['89', '925', 'CF9', 'CA0', 'F18', '4D2']]

print 'Matrix:'

for i in range(6):

    for j in range(6):
        print "%4s(%4s)" % (matrix[i][j], int(matrix[i][j], 16)),
    print ''

print '-------------------------------'

mincost = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0]]

mincost[0][0] = int(matrix[0][0], 16)

for i in range(1, 6):
    mincost[0][i] = mincost[0][i-1] + int(matrix[0][i], 16)

for i in range(1, 6):
    mincost[i][0] = mincost[i-1][0] + int(matrix[i][0], 16)

for i in range(1, 6):

    for j in range(1, 6):
        mincost[i][j] = min(mincost[i-1][j],
                            mincost[i][j-1]) + int(matrix[i][j], 16)

print 'Minimun cost from left/top to right/down: %s' % mincost[5][5]

path = ''

while True:

    if i == 0 and j == 0:
        break

    if i == 0:
        j -= 1
        path += 'r,'
    elif j == 0:
        i -= 1
        path += 'd,'
    elif mincost[i-1][j] < mincost[i][j-1]:
        i -= 1
        path += 'd,'
    elif mincost[i-1][j] > mincost[i][j-1]:
        j -= 1
        path += 'r,'

print 'Path: %s' % path[::-1][1:]
