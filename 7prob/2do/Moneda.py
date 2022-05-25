import random

M=['aguila','sello']

A=0
S=0
X=10

for n in range(X):
    T = random.choice(M)
    if T == 'aguila':
        A+=1
    
    else:
        S+=1

print("Total Aguila: ", A)
print("Total Sello: ", S)