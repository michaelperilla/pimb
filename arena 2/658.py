from sys import stdin
x = (stdin.readline())

x = int(x)
x2 = x/2
x1 = x2%2

x2 = int(x2)
x1 = int(x1)

if(x1 != 0 or x2 >=6 or x2<=20):
    print("Weird")

elif(x1 == 0 and x2 >=2 or x2<=5):
    print("Not Weird")
elif(x1 == 0 and x2>20):
    print("Not Weird")
