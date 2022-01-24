from sys import stdin

def coca(x):
    if(x >= 3):
        return coca(x-2) + 1
    else:
        return 0;

x = int(stdin.readline())
if((x+1)%3 == 0):
    print(str(coca(x+1) + x))
else:
    print(str(coca(x) + x))