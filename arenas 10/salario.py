#jose = 100001
#maria jose = 110001
#raul = 111001
#michael = 111101
empleados=[100001,110001,111001,111101,]
sueldo=[700000, 1200000, 2000000, 700000]
ct = 0

empleados2=[]
sueldo2 =[]
def main():
    x = input("numero de carnet")
    y = input("cuanto gana")

    def empleados1():
        for i in (empleados):
            if(x!=i):
                empleados2.append(empleados + x)
            else:
                res = empleados2
    empleados1()


    def sueldo1():
        ct = 0
        for i in (sueldo):
            if(y>i):
                ct = ct+1
                sueldo2.append(sueldo + (y))
            else:
                sueldo2.append(sueldo + (y))
    sueldo1()

    print("hay",ct,"empleados con el mismo sueldo")
    print((empleados2))
    print((sueldo2))

