p1 = (-1, 3)
p2 = (0, -7)
p3 = (4, 7)
p4 = (5, 11)
x=0


def fn1(p1, p2, p3, p4):
    a: float = ((p1[0]) * (p1[0] - p3[0]) * (p1[0] - p4[0]))
    b: float = p1[1] / a
    c: float = (p3[0]) * (p4[0])
    d: float = b * c
    return d

    

def fn2(p1, p2, p3, p4):
    a: float = ((p1[0]) * (p3[0]) * (p4[0]))
    b: float = p2[1] / a
    c: float = (p1[0]) * (p3[0]) * (p4[0])
    d: float = b * c
    return d


def fn3(p1, p2, p3, p4):
    a: float = ((p3[0] - p1[0]) * (p3[0]) * (p3[0] - p4[0]))
    b: float = p3[1] / a
    c: float = (p1[0])  * (p4[0])
    d: float = b * c
    return c

def fn4(p1, p2, p3, p4):
    a: float = ((p4[0] - p1[0]) * (p4[0]) * (p4[0] - p3[0]))
    b: float = p4[1] / a
    c: float = (p1[0]) * (p3[0])
    d: float = b * c
    return c

print(fn1(p1, p2, p3, p4), 'x3')
print(fn2(p1, p2, p3, p4), 'x2')
print(fn3(p1, p2, p3, p4), 'x')
print(fn4(p1, p2, p3, p4))