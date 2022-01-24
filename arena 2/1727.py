t = input()
mes,dia = t.split(' ')
if(mes == 'JAN' or mes == 'MAR' or mes == 'MAY' or mes == 'JUL' or mes =='AUG' or mes =='OCT' or mes =='DEC'):
    if (dia == 'MON' or dia == 'TUE' or dia=='SUN'):
        print("8")
    elif (dia == 'WED' or dia == 'SAT'):
        print("9")
    elif (dia == 'THU' or dia == 'FRI'):
        print("10")
    else:
        print("ERROR IN DAY!")
elif(mes =='APR' or mes =='JUN' or mes =='SEP' or mes =='NOV'):
    if(dia =='MON' or dia =='TUE' or dia =='WED' or dia == 'SUN'):
        print("8")
    elif(dia == 'SAT' or dia == 'THU'):
        print("9")
    elif(dia == 'FRI'):
        print("10")
    else:
        print("ERROR IN DAY!")
elif(mes == 'FEB'):
    if(dia == 'SAT' or dia == 'FRI' or dia == 'THU' or dia == 'SUN' or dia == 'MON' or dia == 'TUE' or dia == 'WED'):
        print("8")
    else:
        print("ERROR IN DAY!")
else:
    print("ERROR IN MONTH!")