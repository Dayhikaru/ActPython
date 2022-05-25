import matplotlib.pyplot as plp
import numpy as np
from math import sin,sqrt

X = np.arange(0, 10, .10)
Y = (X + sin(2)) * sqrt(9)

print("Puntos X:", X)
print("Puntos Y:", Y)

plp.plot(X,Y)
plp.show()