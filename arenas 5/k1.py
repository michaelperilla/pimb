from sys import stdin
def form ():
    n = int(stdin.readline().strip())
    
    for i in range (n):
        x,y=stdin.readline().strip().split(' ')
        x = int(x)
        y = int(y)
        if (x>y):
           print(">")
        elif(x<y):
           print("<")
        else:
           print("=")
   
form()


nadie le puede pasar algunasA? de estas
