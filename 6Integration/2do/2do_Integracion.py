from math import sin, sqrt


def fn(x):
    return 2 * (sin(sqrt(x)) - x)

a = 0
b = 1.9724
m = (a + b) / 2

r1 = fn(a) * (b - a)
print('Regla del Rectángulo R=', r1)

r2 = fn(m) * (b - a)
print('Regla del punto medio R=', r2)

#########################
def fn1(y):
    return (pow(7, -y)) + 3

c = -1
d = 2
n = (c + d) / 2

r3 = ((d-c) / 2) * (fn1(c) + fn1(d))
print('Regla del Trapecio I=', r3)

r4 = ((d - c) / 6) * (fn1(c) + 4*fn1(n) + fn1(d))
print('Regla de Simpson I=', r4)