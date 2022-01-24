def numeroFeliz(n):
    x = 1
    while n != 1:
        a = 0
        s = str(n)
        for i in range(len(s)):
            a = a + int(s[i]) ** 2
        n = a
        if n == 1:
            return True
        x += 1
        if x == 20:
            return False


for j in range(1, 10):
    if j == 1:
        print(j)
    if numeroFeliz(j):
        print(j)