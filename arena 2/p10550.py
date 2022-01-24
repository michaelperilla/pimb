w= int(input())
x= int(input())
y= int(input())
z= int(input())
if(([w,x,y,z])!=0):
    print(360*2+(w-x+40)%40*9+360+(y-z+40)%40*9+(y-z+40)%40*9)