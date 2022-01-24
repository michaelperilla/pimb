from sys import stdin
x = stdin.readline()

x = int(x)

x1 = x%10
x2 = x//10

x3 = x2%10
x4 = x2//10

x5 = x4%10
x6 = x4//10

x7 = x6%10
x8 = x6//10

if(x>9999):
    print("no se puede")
elif(x1>=x3 and x1>=x5 and x1>=x7):
    print(x1)
elif(x3>=x1 and x3>=x5 and x3>=x7):
    print(x3)
elif(x5>=x1 and x5>=x3 and x5>=x7):
    print(x5)
elif(x7>=x1 and x7>=x3 and x7>=x5):
    print(x7)
