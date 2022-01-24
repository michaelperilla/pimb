x1 = [[5, 4, 2], [2, 130, -12], [0, 0, 0], [9, -31, 10]]
x2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
for i in range(len(x1)):
    for j in range(len(x2)):
        x2[j][i] = x1[i][j]
for i in range(len(x2)):
    print(x2[i])

