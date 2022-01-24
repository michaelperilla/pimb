t = input()
a,b,c,d,e = t.split(' ')

x = int(a+b+c+d+e)
y = str(a*b*c*d*e)
z = int(a-b-c-d-e)

if (x>23 or y>23 or z>23):
    print("possble")
else:
    print("impossible")