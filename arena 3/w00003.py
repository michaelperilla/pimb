from sys import stdin
n = stdin.readline()
n = int(n)

def div(n):
    if (n==1):
        res=1
        print(res)
    else:
        res= int(n/2)
        print(res)
    return res
div()

