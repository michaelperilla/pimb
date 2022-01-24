from sys import stdin

def smoke(n, k):
    if(n >= k):
        return smoke(n-k+1, k) + 1
    else:
        return 0;


n = int(stdin.readline())
k = int(stdin.readline())

total = smoke(n, k) + n
print(str(total))
