def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index+len(char)] == char:
                    return index

            index += 1

    return -1


def buscarMatriz(palabra, lista):
    y = 0
    x = -1
    for linea in lista:
        if x == -1:
            x = find_str(linea, palabra)
            if x == -1:
                x = find_str(linea, palabra[::-1])
            y += 1

    if(x == -1):
        conjunto.write(palabra+': no encontrada\n')
    else:
        conjunto.write(palabra + ': pos('+str(x)+','+str(y)+')\n')


def cargarMatriz():
    lista = []
    matriz = open("matriz.ext", 'r')
    for linea in matriz:
        lista.append(linea[:len(linea) - 1])
    return lista



palabras = open("lista_palabras.ext",'r')
conjunto = open("conjunto.ext",'w')
lista = cargarMatriz()

for palabra in palabras:
    buscarMatriz(palabra[:len(palabra) - 1], lista)

conjunto.close()
palabras.close()




