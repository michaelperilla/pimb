from sys import stdin
def form ():
    n = int(stdin.readline().strip())
    
    for i in range (n):
        x1 ,y1 =stdin.readline().strip().split(' ')
        x = int(x1)
        y = int(y1)
        if (x>y):
           print(">")
        elif(x<y):
           print("<")
        elif(x==y):
           print("=")
   
form()
