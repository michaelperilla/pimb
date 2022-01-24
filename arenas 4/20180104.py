from sys import stdin

n = stdin.readline().strip()
ct = 1
def ope(m):
    global ct
    if (m > 0 and m < 1000000 ) :
        ct *= int(m[0])
        ope(m[1:])


def NumNeto(n):
    global ct
    ope(n)
    if len(str(ct)) == 1:
        if (ct == 0):
            print("Numero Neto")
        else:
            print("No es un Numero Neto")
    return()

def main():
    n = stdin.readline().strip()
    NumNeto(n)

