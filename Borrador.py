import matplotlib.pyplot as plt
from math import sin
def f(x):
    return (1/3)*(x+3)**4+x
def dominio(n):
    R = []
    m = 100
    Dominio = []
    for i in range(m*n,-n):
        R.append([0])
        Dominio.append(i/m)
    c = 0
    for x in Dominio:
        R[c] = x
        #R[c] = round(f(x),1)
        c += 1
    return R
def rango(n):
    R = []
    m = 100
    Dominio = []
    for i in range(m*n,-n):
        R.append([0])
        Dominio.append(i/m)
    c = 0
    for x in Dominio:
        #R[c] = x
        R[c] = round(f(x),3)
        c += 1
    return R
x = dominio(-6)
y = rango(-6)
print('X =',x)
print('Y =',y)
plt.plot(x, y, color='blue', marker='o', linestyle=':', linewidth=1, markersize=1)
plt.show()
