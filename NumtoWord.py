import math


numero = '3665472'


def numerador(numero):
    n = len(numero)-1
    g = math.ceil((n+1)/3)
    M = []
    for i in range(g):
        M.append([0] * 3)

    for i in reversed(range(g)):
        for j in reversed(range(3)):
            if n >= 0:
                M[i][j] = int(numero[n])
                n -= 1
    return M


def palabras(i,j):
    texto = [
            ['', ' UNO', ' DOS', ' TRES', ' CUATRO', ' CINCO', ' SEIS', ' SIETE', ' OCHO', ' NUEVE'],
            ['', ' DIEZ', ' VEINTE', ' TREINTA', ' CUARENTA', ' CINCUENTA', ' SESENTA', ' SETENTA', ' OCHENTA', ' NOVENTA'],
            ['', ' CIEN', ' DOSCIENTOS', ' TRESCIENTOS', ' CUATROCIENTOS', ' QUINIENTOS', ' SEICIENTOS', ' SETECIENTOS',
             ' OCHOCIENTOS', ' NOVECIENTOS']
            ]
    return texto[i][j]


def escritor(numero):
    n = numerador(numero)
    m = len(n)
    t = []
    for i in range(m):
        for j in reversed(range(3)):
            t.append(palabras(j, n[i][2-j]))
    return t


print('------- :: este es el numero introducido: :: ---------')
print(numero)
print('------- :: llenamos en grupos de tres :: --------')
print(numerador(numero))
print('------- :: traducimos aaa palabras :: ---------')
print(escritor(numero))