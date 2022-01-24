x = (input())
def binario ():
    if x == 0:
        return (x)
    else:
        return binario(x // 2) + str(x % 2)
print(binario (x))