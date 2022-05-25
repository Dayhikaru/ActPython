from math import sin

def f(x):
    return ((sin(2*x))**3)/(x**4+1)

x0=2.45

print("Diferencias Finitas Progresivas")

h1=0.5
r1=(f(x0+h1)-f(x0))/h1
print('R1=',r1)

h2=0.3
r2=(f(x0+h2)-f(x0))/h2
print('R2=',r2)

h3=0.1
r3=(f(x0+h3)-f(x0))/h3
print('R3=',r3)

h4=0.00001
r4=(f(x0+h4)-f(x0))/h4
print('R4=',r4)

h5=0.00000001
r5=(f(x0+h5)-f(x0))/h5
print('R5=',r5)

print("\nDiferencias Finitas Centradas")

h1 = 0.5
r1 = (f(x0 + h1) - f(x0 - h1)) / (2 * h1)
print('R1=', r1)

h2=0.3
r2=(f(x0+h2)-f(x0-h2))/(2*h2)
print('R2=',r2)

h3=0.1
r3=(f(x0+h3)-f(x0-h3))/(2*h3)
print('R3=',r3)

h4=0.00001
r4=(f(x0+h4)-f(x0-h4))/(2*h4)
print('R4=',r4)

h5=0.00000001
r5=(f(x0+h5)-f(x0-h5))/(2*h5)
print('R5=',r5)

print("\nDerivada de Primer Orden")

h1=0.5
r1=(f(x0+h1/2)-f(x0-h1/2))/h1
print('R1=', r1)

h2=0.3
r2=(f(x0+h2/2)-f(x0-h2/2))/h2
print('R2=', r2)

h3=0.001
r3=(f(x0+h3/2)-f(x0-h3/2))/h3
print('R3=', r3)

h4=0.000001
r4=(f(x0+h4/2)-f(x0-h4/2))/h4
print('R4=', r4)

h5=0.000000001
r5=(f(x0+h5/2)-f(x0-h5/2))/h5
print('R5=', r5)