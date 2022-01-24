xc = input()

x = int(xc)
ct = 0
lis = []
while(ct < x):

    x = input().strip().split()
    suma +=x

    if (x != 0):
        lis.append(suma)

while(ct<= len(lis)):
    print(str(ct)+': '+str(lis[ct-1]))

