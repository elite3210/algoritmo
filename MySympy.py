from sympy.interactive import printing
from sympy import Limit, limit, Symbol, S

# imprimir con notación matemática.
printing.init_printing(use_latex='mathjax')

x = Symbol('x') # Creando el simbolo x.
Limit(x**2 - x + 2, x, 2) # Creando el objeto Limit

print(Limit(x**2 - x + 2, x, 2).doit())

Limit(1/x, x, S.Infinity)

print(Limit(1/x, x, S.Infinity).doit())