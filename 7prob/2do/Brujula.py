import random

direccion = random.randint(0, 3)

print("Ve al: ")
    
if direccion == 0:
    print("norte")        
elif direccion == 1:
    print("sur")
elif direccion == 2:
    print("oeste")
elif direccion == 3:
    print("este")    