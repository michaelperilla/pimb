elementos = [1,3,5,4,7,9,8,6]
numero = len(elementos)
i= 0
while (i < numero):
    j = i
    while (j < numero):
        if(elementos[i] > elementos[j]):
            temp = elementos[i]
            elementos[i] = elementos[j]
            elementos[j] = temp
        j= j+1
    i=i+1
    print(elementos)
