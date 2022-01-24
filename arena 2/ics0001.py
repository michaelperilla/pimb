from sys import stdin
a ,b ,c = (stdin.readline().strip().split(" "))
a = int(a)
b = int(b)
c = float(c)

#gif
x = (a*b)*8
x1 = x/5
x2 = c*1000000000
x3 = x2/x1

#jpeg
y = (a*b)*24
y1 = y/25
y2 = c*1000000000
y3 = y2/y1

#png
z = (a*b)*24
z1 = z/8
z2 = c*1000000000
z3 = z2/z1

#tiff
f = (a*b)*48
f2 = c*1000000000
f3 = f2/f

x3 = "%.2f"%x3
y3 = "%.2f"%y3
z3 = "%.2f"%z3
f3 = "%.2f"%f3

print(x3,"images in GIF format can be stored")
print(y3,"images in JPEG format can be stored")
print(z3,"images in PNG format can be stored")
print(f3,"images in TIFF format can be stored")