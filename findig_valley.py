from array import *
path=["U","D","D","D","U","D","U","U"]
steps=8
L=0
V=0
for i in path:
    if i == 'U':
        L += 1
        if L == 0:
            V += 1
    else:
        L -= 1
print(V)