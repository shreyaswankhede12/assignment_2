from sympy import *
x=Symbol('x')
y=Symbol('y')
RHS=integrate(1-x)
LHS=integrate(1/(y+1))
print(RHS)
print(LHS)