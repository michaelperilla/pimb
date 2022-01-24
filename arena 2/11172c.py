from sys import stdin
x = int(stdin.readline())
y = int(stdin.readline())

if(x>y):
    print(">")
elif(x<y):
    print("<")
else:
    print("=")