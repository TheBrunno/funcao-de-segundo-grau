from sympy import symbols
from sympy.plotting import plot

def graphCreate(a, b, c):
    x = symbols('x')
    plot(a*(x**2)+(b*x)+c, show=True, xlim=[-5, 5], ylim=[-5, 5])