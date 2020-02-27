from sympy import *


x = symbols('x')
y = symbols('y') #<se especifica el nombre de la variable, x en este caso>
f = atan(15/x)-atan(2/x)                    #<se especifica la expresion de la funcion y se asigna a la variable f>
df1 = diff(f)                               #<calculo de la primera derivada y guardando en la variable df1>

print(df1)
df2 = diff(diff(f))
print(df2)
critical = solve(Eq(df1, 0))               #< find the critical points of f(x), raices, df1 = 0>
print(critical)
df2.subs(x, critical[1])
N(critical[1])
print(N(critical[1]))

print(solveset(Eq(x**2 - 1, 0), x))
print(solve([x**2 - y**2/exp(x)], [x, y], dict=True))
print(solve([sin(x + y), cos(x - y)], [x, y]))
f, g = symbols('f g', cls=Function)
print(f(x))
print(f(x).diff(x))
diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
print(diffeq)
dsolve(diffeq,f(x))
print(dsolve(diffeq,f(x)))
