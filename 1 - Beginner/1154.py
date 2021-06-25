# URI Online Judge 1154

lista = []
X = 0

while X >= 0:
    X = int(input())
    if X >= 0:
        lista.append(X)
    
mean = 0
for item in lista:
    mean += item
    
print('{:.2f}'.format(mean/len(lista)))
