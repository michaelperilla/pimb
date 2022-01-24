def main():
    n = (input("cantidad"))
    n = int(n)
    res = 0
    for i in range(0, n):
        m = int(input("numero"))
        res = res+m
        y = res/n
    print("la sumatoria es",(res))
    print("el promedio es",(y))

main()