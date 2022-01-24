t = input()
x,y = t.split(' ')
m = int(x)
n = int(y)

if(n<0 or m<0):
    print("ERROR")
else:
    x = (m+n)/24
    y = int(x)
    R=(x-y)*24
    print(str(int(round(R,0))))
