x = str.lower(input())

y = list (x)
z = [x[n-1] for n in range(len(x), 0, -1)]
if(y==z):
    print("Correcto")
else:
    print("Incorrecto")