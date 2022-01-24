x = int(input("digite el numero"))
x1 = int(input("digite el numero"))
x2 = int(input("digite el numero"))
x3 = int(input("digite el numero"))
x4 = int(input("digite el numero"))
lis = [x, x1, x2, x3, x4]

for i in range(len(lis)):
    mini = min(lis[i:])
    min_index = lis[i:].index(mini)
    lis[i + min_index] = lis[i]
    lis[i] = mini

print (lis)