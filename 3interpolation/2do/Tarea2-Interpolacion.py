p1 = (-2, 4)
p2 = (-1, -2)
p3 = (3, 5)
p4 = (4.3, 11)
x = 7.7


def fn(x, p1, p2, p3, p4):
    a = ((x - p2[0]) / (p1[0] - p2[0]))
    b = ((x - p3[0]) / (p1[0] - p3[0]))
    c = ((x - p4[0]) / (p1[0] - p4[0]))
    d = a * b * c * p1[1]
    return d

def fn1(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p2[0] - p1[0]))
    b = ((x - p3[0]) / (p2[0] - p3[0]))
    c = ((x - p4[0]) / (p2[0] - p4[0]))
    d = a * b * c * p2[1]
    return d

def fn2(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p3[0] - p1[0]))
    b = ((x - p2[0]) / (p3[0] - p2[0]))
    c = ((x - p4[0]) / (p3[0] - p4[0]))
    d = a * b * c * p3[1]
    return d

def fn3(x, p1, p2, p3, p4):
    a = ((x - p1[0]) / (p4[0] - p1[0]))
    b = ((x - p2[0]) / (p4[0] - p2[0]))
    c = ((x - p3[0]) / (p4[0] - p3[0]))
    d = a * b * c * p4[1]
    return d

def fn4(x, p1, p2, p3, p4):
    return fn(x, p1, p2, p3, p4) + fn1(x, p1, p2, p3, p4) + fn2(x, p1, p2, p3, p4) + fn3(x, p1, p2, p3, p4)

print("X=",x,"\nY=",fn4(x,p1,p2,p3,p4))