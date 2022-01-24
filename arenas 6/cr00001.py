from sys import stdin

entrada = []
total = 0
entrada.append(input())
while(entrada[len(entrada)-1] != '0 0'):
    entrada.append(input())

field = 0
while(total < len(entrada) and entrada[total] != '0 0'):
    xc, yc = entrada[total].split(' ')
    total += 1

    x = int(xc)
    y = int(yc)

    ct = 0
    lis = []

    while (ct < x):
        lis.append(entrada[total])
        total += 1
        ct+=1

    ct = 0
    res = []
    while (ct < x):
        ct2 = 0
        res.append('')
        while(ct2 < y):
            minas = 0
            if(lis[ct][ct2:ct2+1] == '*'):
                res[ct] = res[ct] + '*'
            else:
                p1 = ct -1
                p2 = ct2 -1
                if(p1 >= 0 and p2 >= 0 and lis[p1][p2:p2+1] == '*'):
                    minas += 1

                p1 = ct -1
                p2 = ct2
                if(p1 >= 0 and p2 >= 0 and lis[p1][p2:p2+1] == '*'):
                    minas += 1

                p1 = ct -1
                p2 = ct2 +1
                if(p1 >= 0 and p2 < y and lis[p1][p2:p2+1] == '*'):
                    minas += 1

                p1 = ct
                p2 = ct2 -1
                if (p1 >= 0 and p2 >= 0 and lis[p1][p2:p2 + 1] == '*'):
                    minas += 1

                p1 = ct
                p2 = ct2 + 1
                if (p1 >= 0 and p2 < y and lis[p1][p2:p2 + 1] == '*'):
                    minas += 1

                p1 = ct + 1
                p2 = ct2 - 1
                if (p1 < x and p2 >= 0 and lis[p1][p2:p2 + 1] == '*'):
                    minas += 1

                p1 = ct + 1
                p2 = ct2
                if (p1 < x and p2 >= 0 and lis[p1][p2:p2 + 1] == '*'):
                    minas += 1

                p1 = ct + 1
                p2 = ct2 + 1
                if (p1 < x and p2 < y and lis[p1][p2:p2 + 1] == '*'):
                    minas += 1

                res[ct] = res[ct] + str(minas)

            ct2 += 1
        ct += 1

    field += 1
    if(field != 1):
        print('')

    print('Field #'+str(field)+':')
    ct3 = 0
    while(ct3 < x):
        print(res[ct3])
        ct3 += 1