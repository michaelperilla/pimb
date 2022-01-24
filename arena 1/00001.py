X = int(input(""))
Y = int(input(""))

if(X<0):
    R = '('+int(X)+')+'
else:
    R = int(X)+'+'

if(Y<0):
    R += '('+int(Y)+')'
else:
    R += int(Y)

R += '='+int(X+Y)

print(R)
