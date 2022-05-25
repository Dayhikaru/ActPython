import matplotlib.pyplot as plp
from math import exp

# Función
def f(x):
    return exp(2-x)-7*x

# Derivada
def f2(x): 
    return -exp(2-x)-7

x0=1.5

x1=x0-f(x0)/f2(x0)

x2=x1-f(x1)/f2(x1)

x3=x2-f(x2)/f2(x2)

print('x1 = ',x1,'\nx2 = ',x2,'\nx3 = ',x3,'\nValor =',f(x3),'\nRaiz =',x3)

#Graficas
#Puntos Original
x = [-2, -1, 0, 1, 2]
y = [68.59815, 27.085537, 7.38056, -4.281718, -13]

plp.plot(x, y)
plp.show()

#Puntos Derivada
y1 = [-61.59815, -27.085537, -14.389056, -9.718282, -8]

plp.plot(x, y1)
plp.show()
